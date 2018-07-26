import sys
import os 
import glob


class file_discovery(object):
    
    def __init__(self):
        
        self.yoda_list = []
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
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
                    #array = list(np.empty([len(line_split),width]))
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

files = file_discovery()
yoda_list = files.file_dict
data = store_data(yoda_list)
ret_dict = data.yoda_dict