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

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(CURRENT_DIR)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(CURRENT_DIR))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contur_db.settings")
django.setup()

from analyses.models import dat_database,results_header, histo_header,histo_data,histo_images, dat_files,summary_text


class file_discovery(object):

    def __init__(self, directory, result_name):
        self.dat_list = []
        self.results = None
        self.dir_path = os.path.dirname(os.path.realpath(__file__)) + "/" + directory
        self.db_entry(result_name)

    def db_entry(self,results_name):
        results_obj = results_header.objects.filter(name=results_name).values_list('name')
        if len(results_obj[0]) == 0:
            print("Error: Enter Exisiting Results Object")
        else:
            self.results,created = results_header.objects.get_or_create(name=results_obj[0][0])

        dat_object = dat_database.objects.create(results_object=self.results,
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

    def __init__(self, directory, result_name):
        self.dat_list = []
        self.results = None
        self.dir_path = os.path.dirname(os.path.realpath(__file__)) + "/" + directory
        self.db_entry(result_name)

    def db_entry(self,results_name):
        results_obj = results_header.objects.filter(name=results_name).values_list('name')
        if len(results_obj[0]) == 0:
            print("Error: Enter Exisiting Results Object")
        else:
            self.results,created = results_header.objects.get_or_create(name=results_obj[0][0])

        myfile=""
        for file in glob.glob(self.dir_path + "/index.html"):
            f = open(file)
            myfile = File(f)
            print(file)

        hist_header = histo_header.objects.create(results_object=self.results,uploaded=myfile)
        hist_header.save()


        for file in glob.glob(self.dir_path +"/**/index.html"):
            f = open(file)
            myfile = File(f)
            histogram = histo_data.objects.create(parent=hist_header,dat_store=myfile,
                                                    position=str(str(file.split("/")[-1]).split(".")[0]))
            histogram.save()
            print(file)

        for file in glob.glob(self.dir_path +"/**/*.pdf"):
            f = open(file,mode="rb")
            name = str(file.split("/")[-1]).split(".")[0]
            pdfReader = PyPDF2.PdfFileReader(f)
            myfile = File(pdfReader)
            histogram = histo_data.objects.create(parent=hist_header,
                                                  position=name)
            histogram.dat_store.save('new',myfile)
            histogram.save()
            print(file)

        for file in glob.glob(self.dir_path +"/**/*.png"):
            f = open(file,encoding="ISO8859-1", mode="rb")
            myfile = File(f)
            histogram = histo_images.objects.create(parent=hist_header,
                                                       position=str(file.split("/")[-1]).split(".")[0],image=myfile)
            histogram.save()
            print(file)

if __name__ == "__main__":
    parser = ArgumentParser(description="Upload Yoda Data to Database")
    parser.add_argument('--html','-t')
    parser.add_argument('--directory', '-d')
    parser.add_argument('--results_obj', '-r')
    arguments = parser.parse_args()

    if arguments.html:
        files = html_discovery(arguments.directory, arguments.results_obj)
    else:
        files = file_discovery(arguments.directory,arguments.results_obj)
