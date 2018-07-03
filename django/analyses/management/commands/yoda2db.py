
import os
import glob
from argparse import ArgumentParser
import django
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(CURRENT_DIR)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin")
django.setup()

from analyses.models import Analysis, AnalysisPool,\
                BSM_Model, Used_analyses, Document, Keyword, Linked_keys,\
                runcard, results_header, results_analyses, results_position

class file_discovery(object):

    def __init__(self, directory):

        self.yoda_list = []
        self.dir_path = os.path.dirname(os.path.realpath(__file__)) + "/" + directory
        self.lhcyoda_count = 0
        #self.file_dict = dict()
        self.file_dict = []

        self.get_files()
        self.identify_relevent()

    def get_files(self):
        for filename in glob.iglob(self.dir_path + '/**/*.yoda', recursive=True):
            self.yoda_list.append(filename)


    def identify_relevent(self):
        for item in self.yoda_list:
            address = item.split('/')
            name = address[-1]
            if name == "LHC.yoda" and self.lhcyoda_count == 0:
                self.file_dict.append(item)
                self.lhcyoda_count =+ 1
            if "LHC" not in name:
                self.file_dict.append(item)


class store_data(object):

    def __init__(self,file_dict):
        self.file_dict = file_dict
        self.yoda_dict = dict()
        self.entry = 0
        self.read_yoda()


    def read_yoda(self):
        for file_name in self.file_dict:
            self.file_id = file_name.split("/")[-1].replace(".yoda","")
            self.yoda_dict[self.file_id] = dict()
            file = open(file_name, 'r')
            split = file.read().split("BEGIN ")
            for item in split:
                title = item.split('\n')[0].split('/')
                self.yoda_dict[self.file_id][self.entry] = dict()
                self.yoda_dict[self.file_id][self.entry]['Type'] = title[0].strip()
                try:
                    self.yoda_dict[self.file_id][self.entry]['Analysis'] = title[1].strip()
                    self.yoda_dict[self.file_id][self.entry]['dxy'] = title[2].strip()
                except(IndexError):
                    if len(title) > 1:
                        self.yoda_dict[self.file_id][self.entry]['Detail'] = title[1].strip()


                lines = item.split('\n')

                if len(lines) > 1:
                    self.read_data(lines,item)
                    self.entry += 1

    def read_data(self,lines,item):
        for line in lines:
            self.read_headers(line)
        for section in item.split('#'):
            line_split = section.split('\n')
            if len(line_split) == 2:
                header = line_split[0].split(':')[0]
                value = line_split[0].split(':')[1]
                self.yoda_dict[self.file_id][self.entry][header] = value
            else:
                table_headers = line_split[0]
                width = len(table_headers.split('\t'))
                if width > 1:
                    i = 0
                    array = [x[:] for x in [[None] * width ] * len(line_split)]
                    for line in line_split:
                        if i > 0:
                            listed = line.split('\t')
                            j = 0
                            for item in listed:
                                try:
                                    array[i-1][j] = float(item)
                                except(ValueError):
                                    array[i-1][j] = str(item)
                                j += 1
                        i += 1
                    self.yoda_dict[self.file_id][self.entry][table_headers] = array

    def read_headers(self,line):
        for header in ['Path','Title','Type','XLabel','YLabel','ScaledBy',\
                           'PolyMarker','ErrorBars','LineColor','yodamerge_scale']:
                if header in line:
                    try:
                        self.yoda_dict[self.file_id][self.entry][header] = line.split(':')[1]
                    except(IndexError):
                        self.yoda_dict[self.file_id][self.entry][header] = ''


class db_upload(object):

    def __init__(self,yoda_dict,model_name):
        self.yoda_dict = yoda_dict
        self.model = model_name
        self.upload()

    def upload(self):
        for entry in self.yoda_dict:
            self.upload_header(self.yoda_dict[entry])

    def upload_header(self,input_dict):
        Entry.objects.filter(pub_date__year=2006)

if __name__ == "__main__":
    parser = ArgumentParser(description = "Upload Yoda Data to Database")
    parser.add_argument('--directory', '-d')
    parser.add_argument('--model', '-m')
    arguments= parser.parse_args()

    files = file_discovery(arguments.directory)
    yoda_list = files.file_dict
    data = store_data(yoda_list)
    ret_dict = data.yoda_dict

    print(str(len(ret_dict)) + " Yoda Files Uploaded to Database")
