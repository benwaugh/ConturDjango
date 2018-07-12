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

from analyses.models import map_data, runcard, results_header, map_header

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
        for filename in glob.iglob(self.dir_path + '/**/*.map2.txt', recursive=True):
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
            print(file_name)
            self.file_id = file_name.split("/")[-1].replace(".txt","")
            self.map_dict[self.file_id] = dict()
            with open(file_name, 'r') as myfile:
                data = myfile.read()
            id = 0
            for unedit_line in data.replace("{","").split("}"):
                if len(unedit_line.split(":")) > 2:
                    titles = []
                    datas = []
                    line = unedit_line.replace("]","]:")
                    for i in range(int(len(line.split(":"))/2)):

                        titles.append(line.split(":")[2*i].replace(",","").strip().replace("'",""))
                        datas.append(line.split(":")[2*i+1].strip())

                    self.map_dict[self.file_id][id] = dict()
                    for i in range(len(titles)):
                        self.map_dict[self.file_id][id][titles[i]] = datas[i].replace("[","").replace("]","")
                id += 1


class db_upload(object):

    def __init__(self,map_dict,rc_name):
        self.map_dict = map_dict
        self.i = 0
        self.runcard = rc_name
        self.upload()


    def upload(self):
        header = self.upload_header()
        for item in self.map_dict:
            self.upload_map_position(item,header)


    def upload_header(self):
        db = runcard.objects.filter(runcard_name=str(self.runcard))
        if len(db) == 0:
            print("Runcard Not Found. Please select a runcard from the following list:")
            print(runcard.objects.all())
        else:
            runcard_object,runcard_created = runcard.objects.get_or_create(runcard_name=str(self.runcard))
            results_object = input("Please enter a name for the results object: ")

            upload_header, created_header =\
                results_header.objects.get_or_create(
                    name=str(results_object),
                    runcard=runcard_object,
                    mc_ver="0.0.0",
                    contur_ver="0.0.0",
                    parent=None)

            upload_header.save()
            return upload_header

    def upload_map_position(self,item,header):
        upload_pos, created_position = \
            map_header.objects.get_or_create(analyses=str(item), parent=header)

        upload_pos.save()

        self.upload_map_data(upload_pos, self.map_dict[item], item)


    def upload_map_data(self,header,select_dict,item):
        j = 0
        for term in select_dict:
            row = select_dict[term]
            print(row)
            for i in range(0,len(row['meas'].split(','))):

                    upload_data, created_data = \
                        map_data.objects.get_or_create(
                            model_position = j,
                            meas=row['meas'].split(',')[i],
                            bg=row['bg'].split(',')[i],
                            sErr=row['sErr'].split(',')[i],
                            measErr=row['measErr'].split(',')[i],
                            s=row['s'].split(',')[i],
                            bgErr=row['bgErr'].split(',')[i],
                            kev=row['kev'].split(',')[i],
                            isRatio=row['isRatio'].split(',')[i].strip().replace("'",""),
                            parent=header
                        )

                    upload_data.save()
            j = j + 1


if __name__ == "__main__":
    parser = ArgumentParser(description="Upload Map Data to Database")
    parser.add_argument('--directory', '-d')
    parser.add_argument('--runcard', '-r')
    arguments = parser.parse_args()

    files = file_discovery(arguments.directory)
    map_list = files.file_dict
    data = store_data(map_list)
    map_dict = data.map_dict
    db = db_upload(map_dict, arguments.runcard)
