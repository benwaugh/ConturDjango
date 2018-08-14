import os
import glob
from argparse import ArgumentParser
import django
import sys
from shutil import copyfile
import datetime
from django.core.files import File
import codecs
import PyPDF2
from django.core.files.base import ContentFile
from io import BytesIO


# Get data on current Directory and load Django app
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(CURRENT_DIR)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(CURRENT_DIR))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contur_db.settings")
django.setup()

# Import required models from analyses
from analyses.models import dat_database,results_header, histo_header,histo_data,histo_images, dat_files,summary_text, \
                            results_position
from analyses.management.commands.exceptions import NotFoundInDatabase



class file_discovery(object):

    """
        The file discovery class finds all required dat and Summary txt files,
        before uploading them to the file server and creating the database records.

        Inputs:
            Instance
            String to directory
            Name of corresponding results object
            Name of corresponding position
    """

    def __init__(self, directory, result_name,position):
        # Define class objects
        self.dat_list = []
        self.results = result_name
        self.position = position
        self.dir_path = os.path.dirname(os.path.realpath(__file__)) + "/" + directory
        self.db_entry(result_name)

    def db_entry(self,results_name):
        # Search for results name in database
        results_obj = results_header.objects.filter(name__in=results_name).values_list('name')

        # If not found in database, throw NotFoundInDatabase Error
        # Else create results header
        if len(results_obj[0]) == 0:
            print("Error: Enter Exisiting Results Object")
            raise(NotFoundInDatabase)
        else:
            self.results, created = results_header.objects.get_or_create(name=results_obj[0][0])


        # Create results position as child of results header
        position_obj,position_created = results_position.objects.get_or_create(name=self.position, parent=self.results)
        position_obj.save()
        # Create dat file database object as child of results position
        dat_object = dat_database.objects.create(results_object=position_obj,
                                                                     uploaded=datetime.datetime.now())
        dat_object.save()


        # Search input directory for .dat files, and create objects in fileserver, and records in database
        for file in glob.glob(self.dir_path +"/**/*.dat"):
            f = open(file)
            myfile = File(f)
            created_file = dat_files.objects.create(parent=dat_object,dat_store=myfile,name=str(file.split("/")[-1]))
            created_file.save()


        # Search input directory for .txt files and create objects in fileserver, and records in database
        for file in glob.glob(self.dir_path +"/**/*.txt"):
            f = open(file)
            myfile = File(f)
            created_file = summary_text.objects.create(parent=dat_object,summary_store=myfile)
            created_file.save()

class html_discovery(object):

    """
        The file discovery class finds all required html,pdf and png files,
        before uploading them to the file server and creating the database records.

        Inputs:
            Instance
            String to directory
            Name of corresponding results object
            Name of corresponding position
    """

    def __init__(self, directory, result_name, position):
        # Define class objects
        self.dat_list = []
        self.results = result_name
        self.position = position
        self.dir_path = os.path.dirname(os.path.realpath(__file__)) + "/" + directory
        self.db_entry(result_name)


    def db_entry(self,results_name):
        # Search for results name in database
        results_obj = results_header.objects.filter(name__in=results_name).values_list('name')

        # If not found in database, throw NotFoundInDatabase Error
        # Else create results header
        if len(results_obj[0]) == 0:
            print("Error: Enter Exisiting Results Object")
            raise(NotFoundInDatabase)
        else:
            self.results,created = results_header.objects.get_or_create(name=results_obj[0][0])

        # Create results position as child of results header
        position_obj,position_created = results_position.objects.get_or_create(name=self.position,parent=self.results)

        # Search for index.html (this is the overall index) and create histogram header
        for file in glob.glob(self.dir_path + "/index.html"):
            f = open(file)
            myfile = File(f)

            hist_header = histo_header.objects.create(results_object=position_obj)
            hist_header.uploaded.save("index.html",myfile)
            hist_header.save()


        # Search for index.htmls in subfolders (these are the indexs for the analyses) and create histogram data records
        for file in glob.glob(self.dir_path +"/**/index.html"):
            f = open(file)
            myfile = File(f)
            name = "index.html"
            position = file.split("/")[-2]
            histogram = histo_data.objects.create(parent=hist_header,
                                                    position=position)
            histogram.dat_store.save(name,myfile)
            histogram.save()
            f.close()

        # Search for and upload all pdfs inside directory
        for file in glob.glob(self.dir_path +"/**/*.pdf"):
            f = open(file,'rb')
            name = str(file.split("/")[-1]).split(".")[0] + ".pdf"
            pdf = File(f)
            histogram = histo_data.objects.create(parent=hist_header,position=name)
            histogram.dat_store.save(name,pdf)
            histogram.save()

        # Search for and upload all pngs inside directory
        for file in glob.glob(self.dir_path +"/**/*.png"):
            f = open(file,mode="rb")
            myfile = File(f)
            name = str(str(file.split("/")[-1]).split(".")[0])  + ".png"
            histogram = histo_images.objects.create(parent=hist_header,
                                                       position=name)
            histogram.image.save(name,myfile)


if __name__ == "__main__":
    parser = ArgumentParser(description="Upload Histogram Data or Results to Database")
    parser.add_argument('--html','-t',help='Choose True to search for histogram results (images,htmls), '
                                           'Choose False to search for raw histogram data')
    parser.add_argument('--directory', '-d',help='Directory to search in to find the specified data')
    parser.add_argument('--results_obj', '-r',help='Results object to link results to')
    arguments = parser.parse_args()

    results_obj = results_header.objects.filter(name=arguments.results_obj).values_list('name')

    if arguments.html:
        # Search within directory for files that contain HTML data (contur-plots)
        for root, dirs, files in os.walk(arguments.directory, topdown=False):
            for name in dirs:
                if "contur-plots" in name:
                   position = root.split("/")[-1]
                   files = html_discovery(arguments.directory+position+"/contur-plots/", results_obj, position)
    else:
        # Search within directory for files that contain .dat and summary data (plots and ANALYSIS)
        for root, dirs, files in os.walk(arguments.directory, topdown=False):
            for name in dirs:
                if "ANALYSIS" in name:
                   position = root.split("/")[-1]
                   files = file_discovery(arguments.directory+position, results_obj, position)


