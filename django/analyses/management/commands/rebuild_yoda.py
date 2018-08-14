import os
import glob
from argparse import ArgumentParser
import django
import sys
from collections import OrderedDict
from decimal import Decimal

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(CURRENT_DIR)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(CURRENT_DIR))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contur_db.settings")
django.setup()

from analyses.models import Analysis, AnalysisPool,\
                BSM_Model, Document, Keyword, Linked_keys,\
                runcard, results_header, results_analyses, results_position,\
                overflow_underflow_histo, profile1_data, histo1_data, scatter1_data,\
                scatter2_data, scatter3_data, overflow_underflow_profile, counter

class generate_dict(object):
    """
        This class retrieves all yoda data from the database that is associated to a specific position and adds it to
        a dictionary

        Input:
            id of data to export
    """

    def __init__(self,id):
        # Create class objects
        self.parent = None
        self.data_dict = dict()
        self.export_from_db(id)


    def export_from_db(self,id):
        # Get results position assosiated to input ID
        self.parent = results_position.objects.filter(id=id).values_list('name')
        # Get all children of results position (results analyses)
        children = results_analyses.objects.filter(parent=id)
        # For each child, get data from their children
        for item in children:
            self.retrieve_titles(item)


    def retrieve_titles(self,item):

        # Create start and end titles of yoda data in correct format

        end = "END YODA_" + str(item.Type).upper() + "_V2" + "\n"
        if "Counter" in item.Type:
            name = "BEGIN YODA_COUNTER_V2 /_EVTCOUNT"
        elif "Scatter1D" in item.Type:
            name = "BEGIN YODA_SCATTER1D_V2 /_XSEC"
        else:
            name = "BEGIN YODA_" + str(item.Type).upper() + "_V2 /" + str(item.name) + "/" + str(item.xyd)

        # Create ordered dictionary to store data
        self.data_dict[name] = OrderedDict()

        # Loop through each possible table parameter, add to dictionary if it exists in table (even if ==''), but do
        # not add if its Null in table
        titles =["Path","ScaledBy","Title","Type","XLabel","YLabel",
                 "PolyMarker","ErrorBars","LineColor","yodamerge_scale","mean","area"]
        for title in titles:
            command = "item." + title
            result = eval(command)
            if result is not None:
                if title == "mean":
                    self.data_dict[name]["# Mean"] = result
                elif title == "area":
                    self.data_dict[name]["# Area"] = result
                else:
                    self.data_dict[name][title] = result
        self.data_dict[name]["end"] = end

        # Retrieve table data for corresponding record
        self.retireve_data(item.id,name)



    def retireve_data(self,parent_id,name):

        # Check if values exist for every type of data table
        self.data_dict[name]["data"] = []
        ouh_data = overflow_underflow_histo.objects.filter(parent_id=parent_id)
        profile1 = profile1_data.objects.filter(parent_id=parent_id)
        histo1 = histo1_data.objects.filter(parent_id=parent_id)
        scatter1 = scatter1_data.objects.filter(parent_id=parent_id)
        scatter2 = scatter2_data.objects.filter(parent_id=parent_id)
        scatter3 = scatter3_data.objects.filter(parent_id=parent_id)
        ouf_data = overflow_underflow_profile.objects.filter(parent_id=parent_id)
        counter_data = counter.objects.filter(parent_id=parent_id)
        data_headers = []

        # loop over all data types
        for data_set in (overflow_underflow_histo, profile1_data, histo1_data, scatter1_data,
                scatter2_data, scatter3_data, overflow_underflow_profile, counter):
            string = ""

            # Use metaprogramming to write function to add data to list (if it exists) for every data set in data_set list
            for f in data_set._meta.get_fields():
                if f.verbose_name is not "parent" and f.verbose_name is not "ID":
                    if "row type" in (f.verbose_name):
                        string = string + "ID\t\tID" + "\t\t"
                    else:
                        string = string + str(f.verbose_name) + "\t\t"
            string = string.replace(" n","-")
            string = string.replace(" p","+")
            data_headers.append("# " + string)
        i = -1
        # For each table, add titles to dictionary
        for item in (ouh_data,profile1,histo1,scatter1,scatter2,scatter3,ouf_data,counter_data):

            # Determine if data is for overflow underflow table
            i = i + 1
            ou_bool = False
            if item is ouf_data or item is ouh_data:
                ou_bool = True

            # If data exists for table
            if len(item) > 0:
                # Add title to dict
                title = data_headers[i]
                string = ""
                values_list = item.values_list()

                # Turn values list into large string containing data table, in correct YODA format
                for row in values_list:
                    string = self.get_text(row,string,ou_bool)
                string = title + "\n" + string
                self.data_dict[name]["data"].append(string)
                string = ""



    def get_text(self,row,string,ou_bool):
        # This function transforms the data in the database to the correct format for yoda files
        true_row = row[2:]
        if ou_bool:
            true_row = [true_row[0]] + list(true_row)

        # For value in data row (i.e. loop through values in each row of data)
        for item2 in true_row:
                # If data is not overflow or underflow (since these are strings and dont need to be converted)
                if 'Total' not in str(item2) and 'Underflow' not in str(item2) and 'Overflow' not in str(item2):
                    # Replace blank data with nan (these exist in some scatter 2D plots produced by Yoda)
                    if item2 is None:
                        string = string + "nan" + "\t"
                    else:

                        # Change number to decimal format
                        x = Decimal(float(item2))

                        # Change number to exponential format that yoda uses (i.e 000000e+00)
                        value = str('{:.6e}'.format(x))

                        # Add correct operator (+ or -) to exponential format
                        if abs(x) >= 1:
                            operator = "+"
                        else:
                            if abs(x) == 0:
                                operator = "+"
                            else:
                                operator = "-"

                        # Convert lines that are 0 to correct format
                        if value.count(operator) > 1:
                            power = value.split(operator)[2]
                        else:
                            power = value.split(operator)[1]

                        if len(power) == 1:
                            power = "0" + power

                        if value.split(operator)[0] == '0.000000e':
                            power = "00"

                        # All values back to string
                        value = str(value.split(operator)[0]) + operator + str(power)
                        string = string + value + "\t"


                else:
                    # Add value back to string
                    string = string + item2 + "\t"

        # Add string + new line to table
        string = string + "\n"
        return string

class write_yoda(object):

    """
        This class takes the dictionary created by generate_dict and writes to a file in correct yoda format
    """

    def __init__(self,yoda_dict,file_name):
        # Create class objects
        self.yoda_dict = yoda_dict
        yoda_string = self.create_string(yoda_dict)
        self.write_yoda(file_name,yoda_string)


    def create_string(self,yoda_dict):
        # This function exports all data from the dictionary and writes it to a string that can be written to a yoda file
        yoda_string = ""
        # For each table in yoda dictionary
        for key in yoda_dict:
            yoda_string = yoda_string + key + "\n"

            # For each item in corresponding table in yoda dictionary
            for item in yoda_dict[key]:
                # Write data tables directly from dictionary to string
                if item is "data":
                    for data_set in yoda_dict[key]["data"]:
                        yoda_string = yoda_string + data_set
                else:
                    # Write titles and ending points to string
                    if item is not "end":
                        yoda_string = yoda_string + str(item) + ": " + str(yoda_dict[key][item]) + "\n"
                        if item is "YLabel":
                            yoda_string = yoda_string + "---\n"
                        if "Scatter1D" in yoda_dict[key]['Type'] or "Counter" in yoda_dict[key]['Type']:
                            if "Title" in item:
                                yoda_string = yoda_string + "---\n"

            # Add new line
            yoda_string = yoda_string + yoda_dict[key]["end"] + "\n"
        return yoda_string

    def write_yoda(self,name,string):
        # Write string created in create_string to yoda file
        new_string = ""
        string_split = string.split("\n")
        for line in string_split:
            line_new = line.rstrip()
            new_string = new_string + line_new + "\n"

        reversed_string = ""
        for set in new_string.split("\n\n"):
            reversed_string = set + "\n\n" + reversed_string

        with open(name + ".yoda", "w") as text_file:
            text_file.write(reversed_string)

if __name__ == "__main__":
    parser = ArgumentParser(description="Rebuild Yoda files from database")
    parser.add_argument('--id', '-i',help="Unique ID number of file in yoda position database")
    arguments = parser.parse_args()

    # Generate dictionary from database data
    yoda_create = generate_dict(arguments.id)

    # Retrieve created dictionary
    data_dict = yoda_create.data_dict

    # Get file name
    file_name = yoda_create.parent

    # Write yoda data to file
    write_yoda(data_dict,file_name[0][0])

