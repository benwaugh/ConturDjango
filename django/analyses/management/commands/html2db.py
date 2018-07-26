import os
import glob
from argparse import ArgumentParser
import django
import sys
from shutil import copytree
import datetime
from distutils.dir_util import copy_tree

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(CURRENT_DIR)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(CURRENT_DIR))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contur_db.settings")
django.setup()

from analyses.models import results_header,contur_plots

class copy_directory(object):

    def __init__(self,directory,results):

        self.directory = directory
        self.db_entry(results)
        self.copy_tree(directory)

    def db_entry(self,results_name):

        results_obj = results_header.objects.filter(name=results_name).values_list('name')
        if len(results_obj[0]) == 0:
            print("Error: Enter Exisiting Results Object")
        else:
            self.results,created = results_header.objects.get_or_create(name=results_obj[0][0])

        dat_object,created_obj = contur_plots.objects.get_or_create(results_object=self.results,
                                                                    uploaded=datetime.datetime.now())
        self.id = contur_plots.objects.filter(results_object=self.results,uploaded=datetime.datetime.now()).values_list('id',flat=True)
        dat_object.save()


    def copy_tree(self,directory):
        new_path = "../../../analyses/dat_store/" + str(self.id[0]) + "/htmlplots/"
        #os.makedirs(new_path)
        copytree(directory, new_path)

if __name__ == "__main__":
    parser = ArgumentParser(description="Upload HTML data to internal_file_structure")
    parser.add_argument('--directory', '-d')
    parser.add_argument('--results_obj', '-r')
    arguments = parser.parse_args()

    files = copy_directory(arguments.directory,arguments.results_obj)