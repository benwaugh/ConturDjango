import os
import glob
from argparse import ArgumentParser
import django
import sys
from shutil import copyfile
import datetime

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(CURRENT_DIR)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(CURRENT_DIR))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contur_db.settings")
django.setup()

from analyses.models import dat_database,results_header


class file_discovery(object):

    def __init__(self, directory, result_name):
        self.dat_list = []
        self.results = None
        self.dir_path = os.path.dirname(os.path.realpath(__file__)) + "/" + directory
        self.db_entry(result_name)
        self.get_files()

    def db_entry(self,results_name):
        results_obj = results_header.objects.filter(name=results_name).values_list('name')
        if len(results_obj[0]) == 0:
            print("Error: Enter Exisiting Results Object")
        else:
            self.results,created = results_header.objects.get_or_create(name=results_obj[0][0])

        dat_object,created_obj = dat_database.objects.get_or_create(results_object=self.results,
                                                                    uploaded=datetime.datetime.now())
        self.id = dat_database.objects.filter(results_object=self.results,uploaded=datetime.datetime.now()).values_list('id',flat=True)
        dat_object.save()



    def get_files(self):
        new_path = "../../../analyses/dat_store/" + str(self.id[0]) + "/plots"
        sum_path = "../../../analyses/dat_store/" + str(self.id[0]) + "/ANALYSIS"
        os.makedirs(new_path)
        os.makedirs(sum_path)
        for filename in glob.iglob(self.dir_path + '/**/Plots/*.dat', recursive=True):
            copyfile(filename, new_path + "/" + filename.split("/")[-1])
        for filename in glob.iglob(self.dir_path + "/**/Analysis/summary.txt", recursive=True):
            copyfile(filename, sum_path + "/" + filename.split("/")[-1])




if __name__ == "__main__":
    parser = ArgumentParser(description="Upload Yoda Data to Database")
    parser.add_argument('--directory', '-d')
    parser.add_argument('--results_obj', '-r')
    arguments = parser.parse_args()

    files = file_discovery(arguments.directory,arguments.results_obj)
