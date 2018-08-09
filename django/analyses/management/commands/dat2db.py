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

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(CURRENT_DIR)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(CURRENT_DIR))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contur_db.settings")
django.setup()

from analyses.models import dat_database,results_header, histo_header,histo_data,histo_images, dat_files,summary_text, \
                            results_position


class file_discovery(object):

    def __init__(self, directory, result_name,position):
        self.dat_list = []
        self.results = result_name
        self.position = position
        self.dir_path = os.path.dirname(os.path.realpath(__file__)) + "/" + directory
        self.db_entry(result_name)

    def db_entry(self,results_name):

        results_obj = results_header.objects.filter(name__in=results_name).values_list('name')

        if len(results_obj[0]) == 0:
            print("Error: Enter Exisiting Results Object")
        else:
            self.results, created = results_header.objects.get_or_create(name=results_obj[0][0])


        if len(results_obj[0]) == 0:
            print("Error: Enter Exisiting Results Object")
        else:
            self.results,created = results_header.objects.get_or_create(name=results_obj[0][0])

        position_obj,position_created = results_position.objects.get_or_create(name=self.position, parent=self.results)

        dat_object = dat_database.objects.create(results_object=position_obj,
                                                                     uploaded=datetime.datetime.now())
        dat_object.save()

        for file in glob.glob(self.dir_path +"/**/*.dat"):
            f = open(file)
            myfile = File(f)
            created_file = dat_files.objects.create(parent=dat_object,dat_store=myfile,name=str(file.split("/")[-1]))
            created_file.save()

        for file in glob.glob(self.dir_path +"/**/*.txt"):
            f = open(file)
            myfile = File(f)
            created_file = summary_text.objects.create(parent=dat_object,summary_store=myfile)
            created_file.save()

class html_discovery(object):

    def __init__(self, directory, result_name, position):
        self.dat_list = []
        self.results = result_name
        self.position = position
        self.dir_path = os.path.dirname(os.path.realpath(__file__)) + "/" + directory
        self.db_entry(result_name)


    def db_entry(self,results_name):

        results_obj = results_header.objects.filter(name__in=results_name).values_list('name')

        if len(results_obj[0]) == 0:
            print("Error: Enter Exisiting Results Object")
        else:
            self.results,created = results_header.objects.get_or_create(name=results_obj[0][0])

        position_obj,position_created = results_position.objects.get_or_create(name=self.position,parent=self.results)

        myfile=""
        for file in glob.glob(self.dir_path + "/index.html"):
            f = open(file)
            myfile = File(f)

            hist_header = histo_header.objects.create(results_object=position_obj)
            hist_header.uploaded.save("index.html",myfile)
            hist_header.save()


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
            #print(file)

        for file in glob.glob(self.dir_path +"/**/*.pdf"):
            f = open(file,'rb')
            name = str(file.split("/")[-1]).split(".")[0] + ".pdf"
            pdf = File(f)
            histogram = histo_data.objects.create(parent=hist_header,position=name)
            histogram.dat_store.save(name,pdf)
            histogram.save()
            print(file)

        for file in glob.glob(self.dir_path +"/**/*.png"):
            f = open(file,mode="rb")
            myfile = File(f)
            name = str(str(file.split("/")[-1]).split(".")[0])  + ".png"
            histogram = histo_images.objects.create(parent=hist_header,
                                                       position=name)
            histogram.image.save(name,myfile)
            print(file)

if __name__ == "__main__":
    parser = ArgumentParser(description="Upload Yoda Data to Database")
    parser.add_argument('--html','-t')
    parser.add_argument('--directory', '-d')
    parser.add_argument('--results_obj', '-r')
    arguments = parser.parse_args()

    results_obj = results_header.objects.filter(name=arguments.results_obj).values_list('name')

    if arguments.html:
        for root, dirs, files in os.walk(arguments.directory, topdown=False):
            for name in dirs:
                if "contur-plots" in name:
                   position = root.split("/")[-1]
                   files = html_discovery(arguments.directory+position+"/contur-plots/", results_obj, position)
    else:
        for root, dirs, files in os.walk(arguments.directory, topdown=False):
            for name in dirs:
                if "ANALYSIS" in name:
                   position = root.split("/")[-1]
                   files = file_discovery(arguments.directory+position, results_obj, position)


