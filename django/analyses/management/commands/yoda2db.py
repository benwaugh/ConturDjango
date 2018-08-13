
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
                BSM_Model, used_analyses, Document, Keyword, Linked_keys,\
                runcard, results_header, results_analyses, results_position,\
                overflow_underflow_histo, profile1_data, histo1_data, scatter1_data,\
                scatter2_data, scatter3_data, overflow_underflow_profile, counter
from .exceptions import NotFoundInDatabase

class file_discovery(object):
    """
        This class searches the directory for yoda files and adds them to a dictionary

        Inputs:
            Directory to search in
    """
    def __init__(self, directory):
        # Create class objects
        self.yoda_list = []
        self.dir_path = os.path.dirname(os.path.realpath(__file__)) + "/" + directory
        self.lhcyoda_count = 0
        self.file_dict = []

        self.get_files()
        self.identify_relevent()

    def get_files(self):
        # Search for yoda files in sub directories
        for filename in glob.iglob(self.dir_path + '/**/*.yoda', recursive=True):
            self.yoda_list.append(filename)
        # Search for yoda files in directory
        for filename in glob.iglob(self.dir_path + '/*.yoda', recursive=True):
            self.yoda_list.append(filename)


    def identify_relevent(self):
        # Identify which yoda files are relevent (i.e. do not take an LHC yoda from every folder)
        for item in self.yoda_list:
            address = item.split('/')
            name = address[-1]
            if name == "LHC.yoda" and self.lhcyoda_count == 0:
                self.file_dict.append(item)
                self.lhcyoda_count =+ 1
            if "LHC" not in name:
                self.file_dict.append(item)


class store_data(object):
    """
        This class reads the yoda files and stores it in a dictionary

        Inputs:
            File dictionary from FileDiscovery
    """
    def __init__(self,file_dict):
        # Create class objects
        self.file_dict = file_dict
        self.yoda_dict = dict()
        self.entry = 0
        self.read_yoda()

    def read_yoda(self):
        # Read yoda data from files and assign to relevent areas of the dictionary

        for file_name in self.file_dict:

            # open relevent data from file
            self.file_id = file_name.split("/")[-1].replace(".yoda","")
            self.yoda_dict[self.file_id] = dict()
            file = open(file_name, 'r')

            # Split each section of data by 'BEGIN '
            split = file.read().split("BEGIN ")

            # For each data section store data such as type, analyses, pattern, etc..
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

                # If the section contains a data table, call read_data function to load in to dict
                if len(lines) > 1:
                    self.read_data(lines,item)
                    self.entry += 1

    def read_data(self,lines,item):
        # reads data tables and their metadata in yoda files and adds to dictionary

        # For each line of data in yoda table
        for line in lines:
            # Read the different information about the table (i.e. XLabel,YLabel, Path, etc..)
            self.read_headers(line)

        # Split into tables by hash
        for section in item.split('#'):
            # Split into individual lines
            line_split = section.split('\n')

            # If line has two values only, it is mean or area data.
            if len(line_split) == 2:
                header = line_split[0].split(':')[0].strip()
                value = line_split[0].split(':')[1].strip()
                self.yoda_dict[self.file_id][self.entry][header] = value
            else:
                # If line has more that two values when split, it is a line of data from table

                # Take first row as table headers
                table_headers = line_split[0]

                # Calculate amount of data in row
                width = len(table_headers.split('\t'))
                if width > 1:
                    i = 0
                    # Initialise empty array to store array data
                    array = [x[:] for x in [[None] * width ] * len(line_split)]
                    # For value in line of data, add to position in array
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

                    # Add all of data table to dictionary
                    self.yoda_dict[self.file_id][self.entry][table_headers] = new_array




    def read_headers(self,line):
        # This determines which table parameters are present, which are blank and which have values, and then adds
        # them to the dictionary

        # For each table parameter, search if parameter exists. If parameter exists, add parameter and value (even if
        # Value is blank) to dictionary. If it does not exist then add null field to dictionary
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
    """
    This class takes the yoda dictionary created in read_data and uploads it to the correct areas of the database

    Inputs:
        yoda_dict created in read_data
        name of results object

    """

    def __init__(self,yoda_dict,results_name):
        # Create class objects
        self.yoda_dict = yoda_dict
        self.i = 0
        self.results_name = results_name
        self.upload()


    def upload(self):
        # Create header in database
        header = self.upload_header()
        # Create position object as child of header for each point in parameter space (e.g. mY_100_mX_100)
        for item in self.yoda_dict:
            self.upload_positions(item,header)

    def upload_header(self):
        # Find input results header in database
        db = results_header.objects.filter(name__in=self.results_name)

        # If results header does not exist, throw custom error, otherwise retrieve object.
        if len(db) == 0:
            print("Error: Enter Exisiting Results Object")
            raise (NotFoundInDatabase)
        else:
            results_object, created = results_header.objects.get_or_create(name__in=self.results_name)
            results_object.save()
            return results_object


    def upload_positions(self,position,header):
        # Create results position object for point in parameter space as child of results header.
        upload_pos, created_position = \
            results_position.objects.get_or_create(name=str(position),parent=header)

        upload_pos.save()
        # Call function to upload data from yoda dictionary for current position in parameter space
        self.upload_details(upload_pos,self.yoda_dict[position],position)

    def upload_details(self,upload_position,child_dict,position):
        # This opens the data in the yoda dictionary for a specific positon, and uploads it to the correct area of the
        # database

        # Loop over every item in the dictionary for a point in parameter space
        for record in child_dict:
            select_dict = child_dict[record]

            # Find pattern, mean and area items seperately, since these function different to the other header parameters
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

            # Loop over every possible table parameter and add upload to database for all -> upload none if not in dict
            for term in ['Path', 'Title', 'Type', 'XLabel', 'YLabel', 'ScaledBy', \
             'PolyMarker', 'ErrorBars', 'LineColor', 'yodamerge_scale']:
                if term not in select_dict:
                    select_dict[term] = None

            # Create results_analyses records with data from dictionary
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

            # Call function to upload actual table data
            self.upload_data(upload_info,select_dict)

    def upload_data(self,upload_info,select_dict):
        # This function uploads the data from the tables into the correct data tables in the database
        datas = []
        self.i += 1

        # Loop over every table for selected analyses and pattern in
        for key in select_dict:
            if len(key.split("\t")) > 2:
                datas.append(select_dict[key])


        # If data is 1D histogram data, upload overflow and underflow data and histogram data to database
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

        # If data is 1D profile data, upload overflow and underflow data and profile data to database
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

        # If data is 2D scatter data upload to 2D scatter table
        if select_dict['Type'] == 'Scatter2D':
            for item_list in datas[0]:
                #print(item_list)
                upload_scatter, created_scatter = scatter2_data.objects.get_or_create(
                    parent=upload_info,
                    xval=item_list[0],
                    xerr_n=item_list[1],
                    xerr_p =item_list[2],
                    yval =item_list[3],
                    yerr_n =item_list[4],
                    yerr_p =item_list[5])
                upload_scatter.save()

        # If data is 1D scatter data upload to 1D scatter table
        if select_dict['Type'] == 'Scatter1D':
            for item_list in datas[0]:
                upload_scatter, created_scatter = scatter1_data.objects.get_or_create(
                    parent=upload_info,
                    xval=item_list[0],
                    xerr_n=item_list[1],
                    xerr_p=item_list[2])
                upload_scatter.save()

        # If data is 3D scatter data upload to 3D scatter table (does not currently exist but built in incase it is
        # required in the future)
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

        # If data is event counter, upload to counter table
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
    parser.add_argument('--directory', '-d',help='Directory to search in to find the specified data')
    parser.add_argument('--results','-o',help='Corresponding results object')
    arguments = parser.parse_args()


    # Find Yoda files in specified directory
    files = file_discovery(arguments.directory)

    # Retrieve created file dictionary
    yoda_list = files.file_dict

    # Upload all yoda data to dictionary
    data = store_data(yoda_list)

    # Retrieve created yoda dictionary
    ret_dict = data.yoda_dict

    # Upload dictionary data to database
    db = db_upload(ret_dict,arguments.results)

    print(str(len(ret_dict)) + " Yoda Files Uploaded to Database")
