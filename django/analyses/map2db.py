import os
import glob
from argparse import ArgumentParser
import django
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(CURRENT_DIR)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(CURRENT_DIR))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contur_db.settings")
django.setup()

from analyses.models import map_data

class file_discovery(object):

    def __init__(self, directory):

        self.map_list = []
        self.dir_path = os.path.dirname(os.path.realpath(__file__)) + "/" + directory
        self.map_count = 0
        self.file_dict = []

        self.get_files()
        self.identify_relevent()

    def get_files(self):
        print(self.dir_path)
        for filename in glob.iglob(self.dir_path + '/**/*.map2', recursive=True):
            self.map_list.append(filename)

    def identify_relevent(self):
        for item in self.map_list:
            address = item.split('/')
            name = address[-1]
            self.file_dict.append(item)

class store_data(object):

    def __init__(self,file_dict):
        self.file_dict = file_dict
        self.map_dict = dict()
        self.entry = 0
        self.read_map()

    def read_map(self):
        for file_name in self.file_dict:
            self.file_id = file_name.split("/")[-1].replace(".map2","")
            self.map_dict[self.file_id] = dict()
            file = open(file_name, 'r')
            split = dict(file.read())
            print(split['meas'])

if __name__ == "__main__":
    parser = ArgumentParser(description="Upload Map Data to Database")
    parser.add_argument('--directory', '-d')
    #parser.add_argument('--runcard', '-r')
    arguments = parser.parse_args()

    files = file_discovery(arguments.directory)
    map_list = files.file_dict
