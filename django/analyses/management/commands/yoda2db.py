
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

from analyses.models import Analysis, AnalysisPool,\
                BSM_Model, Used_analyses, Document, Keyword, Linked_keys,\
                runcard, results_header, results_analyses, results_position,\
                overflow_underflow_histo, profile1_data, histo1_data, scatter1_data,\
                scatter2_data, scatter3_data, overflow_underflow_profile, counter


class file_discovery(object):

    def __init__(self, directory):

        self.yoda_list = []
        self.dir_path = os.path.dirname(os.path.realpath(__file__)) + "/" + directory
        self.lhcyoda_count = 0
        self.file_dict = []

        self.get_files()
        self.identify_relevent()

    def get_files(self):
        print(self.dir_path)
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
                header = line_split[0].split(':')[0].strip()
                value = line_split[0].split(':')[1].strip()
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
                    new_array = []
                    for row in array:
                        if None not in row:
                            new_array.append(row)
                    self.yoda_dict[self.file_id][self.entry][table_headers] = new_array




    def read_headers(self,line):
        for header in ['Path', 'Title', 'Type', 'XLabel', 'YLabel', 'ScaledBy', \
                        'PolyMarker', 'ErrorBars', 'LineColor', 'yodamerge_scale']:
                if header in line:
                    try:
                        value = line.split(':')[1]
                        try:
                            value = value.strip()
                        except(TypeError):
                            value = float(value)
                        self.yoda_dict[self.file_id][self.entry][header] = value
                    except(IndexError):
                        self.yoda_dict[self.file_id][self.entry][header] = ''


class db_upload(object):

    def __init__(self,yoda_dict,rc_name):
        self.yoda_dict = yoda_dict
        self.i = 0
        self.runcard = rc_name
        self.upload()


    def upload(self):
        header = self.upload_header()
        for item in self.yoda_dict:
            self.upload_positions(item,header)

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


    def upload_positions(self,position,header):
        print(header)
        upload_pos, created_position = \
            results_position.objects.get_or_create(name=str(position),parent=header)

        upload_pos.save()
        self.upload_details(upload_pos,self.yoda_dict[position],position)

    def upload_details(self,upload_position,child_dict,position):
        for record in child_dict:

            select_dict = child_dict[record]

            if 'dxy' not in select_dict:
                dxy = None
            else:
                dxy = select_dict['dxy']

            if 'Mean' in select_dict:
                mean = select_dict['Mean']
            else:
                mean = float("nan")

            if 'Area' in select_dict:
                area = select_dict['Area']
            else:
                area = float("nan")

            for term in ['Path', 'Title', 'Type', 'XLabel', 'YLabel', 'ScaledBy', \
             'PolyMarker', 'ErrorBars', 'LineColor', 'yodamerge_scale']:
                if term not in select_dict:
                    select_dict[term] = None

            upload_info, created_info = \
                results_analyses.objects.get_or_create(
                    name=select_dict['Analysis'],
                    parent=upload_position,
                    xyd=dxy,
                    Path=select_dict['Path'],
                    Title=select_dict['Title'],
                    Type=select_dict['Type'],
                    XLabel=select_dict['XLabel'],
                    YLabel=select_dict['YLabel'],
                    ScaledBy=select_dict['ScaledBy'],
                    PolyMarker=select_dict['PolyMarker'],
                    ErrorBars=select_dict['ErrorBars'],
                    LineColor=select_dict['LineColor'],
                    yodamerge_scale=select_dict['yodamerge_scale'],
                    mean=mean,
                    area=area,
                    )
            upload_info.save()

            self.upload_data(upload_info,select_dict)

    def upload_data(self,upload_info,select_dict):
        datas = []
        self.i += 1
        print(self.i)

        for key in select_dict:
            if len(key.split("\t")) > 2:
                datas.append(select_dict[key])

        if select_dict['Type'] == 'Histo1D':
            for item_list in datas[0]:
                    upload_ou,created_ou = overflow_underflow_histo.objects.get_or_create(
                    parent = upload_info,
                    row_type = item_list[0],
                    sumw = item_list[2],
                    sumw2= item_list[3],
                    sumwx = item_list[4],
                    sumwx2 = item_list[5],
                    numEntries = item_list[6])
                    upload_ou.save()
            for item_list in datas[1]:
                    upload_hist, created_hist = histo1_data.objects.get_or_create(
                        parent=upload_info,
                        xlow=item_list[0],
                        xhigh=item_list[1],
                        sumw=item_list[2],
                        sumw2=item_list[3],
                        sumwx=item_list[4],
                        sumwx2=item_list[5],
                        numEntries=item_list[6])
                    upload_hist.save()

        if select_dict['Type'] == 'Profile1D':
            for item_list in datas[0]:
                upload_ou, created_ou = overflow_underflow_profile.objects.get_or_create(
                    parent=upload_info,
                    row_type=item_list[0],
                    sumw=item_list[2],
                    sumw2=item_list[3],
                    sumwx=item_list[4],
                    sumwx2=item_list[5],
                    sumwy=item_list[6],
                    sumwy2=item_list[7],
                    numEntries=item_list[8])
                upload_ou.save()

            for item_list in datas[1]:
                upload_prof, created_prof = profile1_data.objects.get_or_create(
                    parent=upload_info,
                    xlow=item_list[0],
                    xhigh=item_list[1],
                    sumw=item_list[2],
                    sumw2=item_list[3],
                    sumwx=item_list[4],
                    sumwx2=item_list[5],
                    sumwy=item_list[6],
                    sumwy2=item_list[7],
                    numEntries=item_list[8])
                upload_prof.save()


        if select_dict['Type'] == 'Scatter2D':
            for item_list in datas[0]:
                upload_scatter, created_scatter = scatter2_data.objects.get_or_create(
                    parent=upload_info,
                    xval=item_list[0],
                    xerr_n=item_list[1],
                    xerr_p =item_list[2],
                    yval =item_list[3],
                    yerr_n =item_list[4],
                    yerr_p =item_list[5])
                upload_scatter.save()

        if select_dict['Type'] == 'Scatter1D':
            for item_list in datas[0]:
                upload_scatter, created_scatter = scatter1_data.objects.get_or_create(
                    parent=upload_info,
                    xval=item_list[0],
                    xerr_n=item_list[1],
                    xerr_p=item_list[2])
                upload_scatter.save()

        if select_dict['Type'] == 'Scatter3D':
            for item_list in datas[0]:
                upload_scatter, created_scatter = scatter3_data.objects.get_or_create(
                    parent=upload_info,
                    xval=item_list[0],
                    xerr_n=item_list[1],
                    xerr_p=item_list[2],
                    yval=item_list[3],
                    yerr_n=item_list[4],
                    yerr_p=item_list[5],
                    zval=item_list[6],
                    zerr_n=item_list[7],
                    zerr_p=item_list[8])
                upload_scatter.save()

        if select_dict['Type'] == 'Counter':
            for item_list in datas[0]:
                upload_counter, created_counter = counter.objects.get_or_create(
                    parent=upload_info,
                    sumw=item_list[0],
                    sumw2=item_list[1],
                    numEntries=item_list[2])
                upload_counter.save()





if __name__ == "__main__":
    parser = ArgumentParser(description="Upload Yoda Data to Database")
    parser.add_argument('--directory', '-d')
    parser.add_argument('--runcard', '-r')
    arguments = parser.parse_args()

    files = file_discovery(arguments.directory)
    yoda_list = files.file_dict
    data = store_data(yoda_list)
    ret_dict = data.yoda_dict
    db = db_upload(ret_dict, arguments.runcard)

    print(str(len(ret_dict)) + " Yoda Files Uploaded to Database")
