import os
import glob
from argparse import ArgumentParser
import django
import sys
import pickle

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(CURRENT_DIR)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(CURRENT_DIR))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contur_db.settings")
django.setup()

from analyses.models import runcard, results_header, map_header, map_pickle
from analyses.management.commands.exceptions import NotFoundInDatabase

class file_discovery(object):

    """
        This class searches for the required .map file in the specified directory

        Inputs:
            Directory to search in
    """

    def __init__(self, directory):
        # Create class objects
        self.map_list = []
        self.dir_path = os.path.dirname(os.path.realpath(__file__)) + "/" + directory
        self.map_count = 0
        self.file_dict = []

        self.get_files()
        self.identify_relevent()

    def get_files(self):
        """
            Searches for .map files and adds them to a list
        """
        for filename in glob.iglob(self.dir_path + '/*.map', recursive=True):
            self.map_list.append(filename)
        for filename in glob.iglob(self.dir_path + '/.map', recursive=True):
            self.map_list.append(filename)

    def identify_relevent(self):
        """
            Identifies names of files and adds them to a file dictionary
        """
        for item in self.map_list:
            address = item.split('/')
            name = address[-1]
            self.file_dict.append(item)


class store_data(object):
    """
        This class creates reads in the files identified in FileDiscovery and creates a dictionary of the filename and
        data

        Inputs:
            File_dict from FileDiscovery
    """


    def __init__(self,file_dict):
        # Create class objects
        self.file_dict = file_dict
        self.map_dict = dict()
        self.entry = 0
        self.read_map()

    def read_map(self):
        """
            Opens pickled files, decodes data and saves to dictionary
        """
        for file_name in self.file_dict:
            self.file_id = file_name.split("/")[-1]
            if str(self.file_id) == ".map":
                self.file_id = "heatmap"
            self.file_id = self.file_id.replace(".map","")

            with open(file_name, 'r+b') as myfile:
                data = pickle.load(myfile)
                self.map_dict[self.file_id] = data


class db_upload(object):
    """
        This class takes the dictionary created in the store_data class and uploads it to the database

        Inputs:
            map_dict: Dictionary created in store_data
            results_name: Name of results object
    """


    def __init__(self,map_dict,results_name):
        # Create class objects
        self.map_dict = map_dict
        self.i = 0
        self.results_name = results_name
        self.upload()

    def upload(self):
        # Create map header
        header = self.upload_header()
        for item in self.map_dict:
            self.upload_map_position(item,header)


    def upload_header(self):
        # Create map header record in database using results name
        try:
            results_object = results_header.objects.get(name=self.results_name)
            # If results header does not exist, throw custom error, otherwise retrieve object.
        except:
            print("Error: Enter Exisiting Results Object.")
            print("Existing Results Objects:" + str(results_header.objects.all()))
            raise (NotFoundInDatabase)
        return results_object

        return results_object

    def upload_map_position(self,item,header):
        # Retrieve map header
        upload_pos, created_position = \
            map_header.objects.get_or_create(analyses=str(item), parent=header)

        upload_pos.save()

        # Upload data from dictionary
        self.upload_map_data(upload_pos, self.map_dict[item], item)


    def upload_map_data(self,header,select_dict,item):
        # Create object in database and upload pickle data
        upload_object, created_object = \
                            map_pickle.objects.get_or_create(
                                parent=header,
                                pickle=select_dict,
                         )
        upload_object.save()


if __name__ == "__main__":
    parser = ArgumentParser(description="Upload Map Data to Database")
    parser.add_argument('--directory', '-d',help='Directory to search in to find the specified data')
    parser.add_argument('--results','-r',help='Corresponding results object')
    arguments = parser.parse_args()

    # Run file discovery to find relevent files
    files = file_discovery(arguments.directory)

    # Get out resulting file dictionary
    map_list = files.file_dict

    # Open and depickle map data into dictionary
    data = store_data(map_list)

    # Get out created dictionary
    map_dict = data.map_dict

    # Upload data from dictionary to database, linked to results header
    db = db_upload(map_dict,arguments.results)


