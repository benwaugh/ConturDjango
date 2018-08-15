# Models.py: This defines all Django Models. These correspond to tables and columns within the database.
# This is a vital component of the Model-View-Template design pattern, and defines all data structures used.

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from mptt.models import MPTTModel, TreeForeignKey
from picklefield.fields import PickledObjectField



@python_2_unicode_compatible
class Analysis(models.Model):
    """
        Contains definition of Analysis model

        Analysis is linked to different models across the app:
        - Used to link Analyses to corresponding .ana files
        - Used to link Keywords to each Analyses
        - Used to link blacklist,subpool ,whitelist and normalisation to analyses

        Parameters:
        anaid (str): [Primary Key]: Name of Analyses: Should correspond to name in Rivet or HEPData
        lumi (float): Luminosity: Luminosity for given analysis
        pool ('Analysis Pool'): Pool that analysis corresponds to.
                                        [This is a foreign key link to the 'AnalysisPool' field]

        Returns:
            anaid

        db_table:
            analysis

    """
    anaid = models.TextField(primary_key=True)
    lumi = models.FloatField()
    pool = models.ForeignKey('AnalysisPool', models.DO_NOTHING, db_column='pool', blank=True, null=True)
    def __str__(self):
        return self.anaid

    class Meta:
        db_table = 'analysis'



@python_2_unicode_compatible
class AnalysisPool(models.Model):
    """
        Contains definition of AnalysisPool model

        AnalysisPool is linked to different models across the app:
        - Used to link Pool to Analysis

        Parameters:
        pool (str): [Primary Key]: Name of Pool

        Returns:
            pool

        db_table:
            analysis_pool

    """
    pool = models.TextField(primary_key=True)
    def __str__(self):
        return self.pool

    class Meta:
        db_table = 'analysis_pool'



@python_2_unicode_compatible
class Blacklist(models.Model):
    """
        Contains definition of Blacklist model

        Parameters:
        id (int): [Primary Key]
        anaid ('Analysis'): Analysis that Blacklist corresponds to.
                                        [This is a foreign key link to the 'Analysis' field]
        pattern (str): Pattern to be excluded

        Returns:
            anaid pattern

        db_table:
            blacklist

        """
    anaid = models.ForeignKey(Analysis, models.DO_NOTHING, db_column='anaid')
    pattern = models.TextField()
    def __str__(self):
        return '%s %s' % (self.anaid, self.pattern)

    class Meta:
        db_table = 'blacklist'



@python_2_unicode_compatible
class Normalization(models.Model):
    """
        Contains definition of Normalization model

        Parameters:
        id (int): [Primary Key]
        anaid ('Analysis'): Analysis that Normalization corresponds to.
                                        [This is a foreign key link to the 'Analysis' field]
        pattern (str): Pattern to be normalized
        norm (float): normalization factor
        scalemc (int): scale factor

        Returns:
            anaid pattern

        db_table:
            normalization

        """
    anaid = models.ForeignKey(Analysis, models.DO_NOTHING, db_column='anaid')
    pattern = models.TextField()
    norm = models.FloatField()
    scalemc = models.IntegerField()
    def __str__(self):
        return '%s %s' % (self.anaid, self.pattern)

    class Meta:
        db_table = 'normalization'
        unique_together = (('anaid', 'pattern'),)



@python_2_unicode_compatible
class Subpool(models.Model):
    """
        Contains definition of Subpool model

        Parameters:
        id (int): [Primary Key]
        anaid ('Analysis'): Analysis that Subpool corresponds to.
                                        [This is a foreign key link to the 'Analysis' field]
        pattern (str): Pattern corresponding to subpool
        subanaid (int): id of sub-analysis

        Returns:
            anaid pattern

        db_table:
            subpool

    """
    anaid = models.ForeignKey(Analysis, models.DO_NOTHING, db_column='anaid')
    pattern = models.TextField()
    subanaid = models.IntegerField()
    def __str__(self):
        return '%s %s' % (self.anaid, self.pattern)

    class Meta:
        db_table = 'subpool'
        unique_together = (('anaid', 'pattern'),)



@python_2_unicode_compatible
class Whitelist(models.Model):
    """
        Contains definition of Whitelist model

        Parameters:
        id (int): [Primary Key]
        anaid ('Analysis'): Analysis that Whitelist corresponds to.
                                        [This is a foreign key link to the 'Analysis' field]
        pattern (str): Pattern to be included

        Returns:
            anaid pattern

        db_table:
            whitelist

    """
    anaid = models.ForeignKey(Analysis, models.DO_NOTHING, db_column='anaid')
    pattern = models.TextField()
    def __str__(self):
        return '%s %s' % (self.anaid, self.pattern)

    class Meta:
        db_table = 'whitelist'



@python_2_unicode_compatible
class BSM_Model(models.Model):
    """
        Contains definition of BSM model:
            This represents the header of model, which links to runcards and then indirectly to results.
            This means that every result can be easily linked to the model header for querying and comparisons

        BSM_Model is linked to different models across the app:
        - Linked to used_analyses to link ana files to models
        - Linked to Download to select BSM model to download
        - Linked to Runcard to link individual runs to model header

        Parameters:
        name (str): [Primary Key]: Name Model
        UFO_Link (str): Link to feynrules raw download of UFO model -> This is used to download the model to the django files
        author (str): Name of creator -> used for Personal dashboard
        date_downloaded (DateTime): date created

        Returns:
            name

        db_table:
            bsm_model

    """
    name = models.CharField(max_length=100,primary_key=True)
    UFO_Link = models.TextField(blank=True)
    author = models.CharField(max_length=50)
    date_downloaded = models.DateField()


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bsm_model'



@python_2_unicode_compatible
class used_analyses(models.Model):
    """
        Contains definition of used_analyses model:
            One of 3 models used to link models, ana files and analyses together

        used_analyses is not directly linked to any models

        Parameters:
        id (int): [Primary Key]
        ana_name ('ana_list'): Corresponding ana file
                                        [This is a foreign key link to the 'ana_list' field]
        modelname ('BSM_Model'): Corresponding BSM_Model
                                        [This is a foreign key link to the 'BSM_Model' field]

        Returns:
            ana_name

        db_table:
            used_analyses

    """
    ana_name = models.ForeignKey('ana_list', models.DO_NOTHING, db_column='ana_name', blank=False, null=False)
    modelname = models.ForeignKey('BSM_Model', models.DO_NOTHING, db_column='model', blank=False, null=False)

    def __str__(self):
        return self.ana_name

    class Meta:
        db_table = 'used_analyses'
        unique_together = (('modelname', 'ana_name'),)

class ana_file(models.Model):
    """
        Contains definition of ana_file model:
            One of 3 models used to link models, ana files and analyses together

        ana_file is not directly linked to any models

        Parameters:
        id (int): [Primary Key]
        ana_name ('ana_list'): Corresponding ana file
                                        [This is a foreign key link to the 'ana_list' field]
        anaid ('Analysis'): Corresponding Analysis
                                        [This is a foreign key link to the 'Analysis' field]

        Returns:
            linked_ana-anaid

        db_table:
            ana_file

    """
    linked_ana = models.ForeignKey('ana_list', models.DO_NOTHING, db_column='linked_ana', blank=False, null=False)
    anaid = models.ForeignKey('Analysis', models.DO_NOTHING, db_column='anaid', blank=False, null=False)

    def __str__(self):
        return '%s-%s' % (self.linked_ana, self.anaid)

    class Meta:
        db_table = 'ana_file'

class ana_list(models.Model):
    """
        Contains definition of ana_list model:
            One of 3 models used to link models, ana files and analyses together
            Defines all ana file names

        ana_list is linked to different models across the app:
        - Linked to used_analyses to match ana files to the models they are used in
        - Linked to ana_file to match file names to the analyses within them

        Parameters:
        id (int): [Primary Key]
        ana_name (str): .ana file name
        author (str): name of creator

        Returns:
            linked_ana anaid

        db_table:
            analyses_ana_list

    """
    ana_name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.ana_name



@python_2_unicode_compatible
class Download(models.Model):
    now = datetime.datetime.now()
    runcard_name = models.CharField(max_length=200, default=now.strftime("%d%m%Y%H%M"),primary_key=True)
    FILE_CHOICES = zip(BSM_Model.objects.all().values_list('name', flat=True) [0::1], BSM_Model.objects.all().values_list('name', flat=True)[0::1])
    Model = models.CharField(max_length=200, choices=FILE_CHOICES, default='')
    Parameter_Card = models.FileField(upload_to='analyses/parameters-cards/', default='')



@python_2_unicode_compatible
class Document(models.Model):
    a = 1



@python_2_unicode_compatible
class Keyword(models.Model):
    """
        Contains definition of Keyword model

        Keyword is linked to Linked_Keys model

        Parameters:
        key_word (str): key word collected from inspire

        Returns:
            keyword

        db_table:
            keywords_list

    """
    key_word = models.TextField(primary_key=True)

    def __str__(self):
        return self.key_word

    class Meta:
        db_table = 'keywords_list'



@python_2_unicode_compatible
class Linked_keys(models.Model):
    """
        Contains definition of Linked_keys model:
            Links keywords to analyses

        Linked_keys is not directly linked to any models

        Parameters:
        id (int): [Primary Key]
        anaid ('Analysis'): Corresponding Analysis
                                        [This is a foreign key link to the 'Analysis' field]
        key_word ('Keyword'): Corresponding Keyword
                                        [This is a foreign key link to the 'Keyword' field]

        Returns:
            key_word anaid

        db_table:
            linked_keywords

    """
    anaid = models.ForeignKey('Analysis', models.DO_NOTHING, db_column='anaid', blank=False, null=False)
    key_word = models.ForeignKey('Keyword', models.DO_NOTHING, db_column='keyword', blank=False, null=False)
    def __str__(self):
        return '%s %s' % (self.key_word, self.anaid)

    class Meta:
        db_table = 'linked_keywords'
        unique_together = (('key_word', 'anaid'),)



@python_2_unicode_compatible
class runcard(models.Model):
    """
        Contains definition of Runcard model:
            Represents a single contur run, linked to a BSM model and ana files, and is then linked to results objects


        BSM_Model is linked to results header

        Parameters:
        now (DateTime): created time
        author (str): Creator of Runcard
        runcard_name (str):[Primary Key]: Name of Runcard: Defaults to current time in string format to give unique name
        modelname ('BSM Model'): Link to corresponding BSM Model
                                    [This is a foreign key link to the 'BSM_Model' field]
        param_card (str): Text containing parameter card in plain text

        Returns:
            runcard_name

        db_table:
            analyses_runcard

    """
    now = datetime.datetime.now()
    author = models.CharField(max_length = 50, default="Contur User")
    runcard_name = models.CharField(max_length=50, default=now.strftime("%d%m%Y%H%M"),primary_key=True)
    modelname = models.ForeignKey('BSM_Model', models.DO_NOTHING, db_column='name', blank=False, null=False)
    param_card = models.TextField(max_length=500)

    def __str__(self):
        return self.runcard_name

    class Meta:
        db_table = 'runcard_export'
        unique_together = (('runcard_name', 'param_card'),)




# Define Modified Preorder Tree Traversal  Structure
class results_header(MPTTModel):
    """
       Contains definition of results_header MPTTmodel:
            This is the top of the MPTT, and links to all results data below it


       results_header is parent to:
            - results position
            - map header
            - histo header

       Parameters:
       author (str): Creator of results object
       name (str): name of the results object
       runcard ('runcard'): The linked runcard
                            [This is a foreign key link to the 'BSM_Model' field]
       mc_ver ('str'): Monte Carlo generator version
       contur_ver ('str'): Contur Version
       parent ('str'): Blank field, top level has no parent
       type ('str'): Describes if plot is Histogram or Heatmap (unused field)

       Returns:
           name

        db_table:
            analyses_results_header

   """
    author = models.CharField(max_length=50, default="Contur User")
    name = models.CharField(max_length=50, unique=True,primary_key=True)
    runcard = models.ForeignKey('runcard', models.DO_NOTHING, db_column='runcard_name', blank=False, null=False,default='')
    herwig_ver = models.CharField(max_length=20, default='0.0.0')
    contur_ver = models.CharField(max_length=20, default='0.0.0')
    rivet_ver = models.CharField(max_length=20, default='0.0.0')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='results')
    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class results_position(MPTTModel):
    """
       Contains definition of results_position MPTTmodel:
            This shows the position in parameter space (i.e. the two parameters used and their values)


       results_position is parent to:
            - results Analyses

       Parameters:
       ID (int): [Primary Key]
       name (str): Position (also name of yoda file)
       parent ('results_header'): results header parent to this position
                        [This is a tree foreign key link to the 'results_header' field]

       Returns:
            name

       db_table:
            analyses_results_position

   """
    name = models.CharField(max_length=50,unique=False)
    parent = TreeForeignKey('results_header', on_delete=models.CASCADE, null=False, blank=True, related_name='position')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class results_analyses(MPTTModel):
    """
       Contains definition of results_analyses MPTTmodel:
            This shows the analyses that the results come from


       results_position is parent to:
            - Scatter data (1D,2D,3D) : 3 Models
            - Histogram data (1D) : 1 Model
            - Profile data (1D) : 1 Model
            - Overflow Underflow Tables (Histo and Profile): 2 Models
            - Counter data: 1 Model



       This model represents all header data within yoda files. Since some data is blank for yoda entries, and some has
       the fields missing altogether, a blank field is used to represent a blank entry, and a null field is used to
       represent a missing field.


       Parameters:
       ID (int): [Primary Key]
       name (str): Name of analyses (can be directly linked to analyses model, but seperated for now)
       parent ('results_position'): results position parent to this analyses
                        [This is a tree foreign key link to the 'results_position' field]
       xyd (str): Pattern position (i.e. x02-y01-d07)
       Path (str): Path to image when created
       Title (str): Title of plot
       Type (str): Type of plot (i.e. Histo1D, Scatter2D)
       XLabel (str): Label of X axis on plot
       YLabel (str): Label of Y axis on plot
       ScaledBy (str): Scaling on plot
       PolyMarker (str): Characters to represent plotting instructions to Yoda
       ErrorBars (str): Error bar details
       LineColor (str): Colour of lines
       yodamerge_scale (str): scaling factor
       mean (float): mean of data
       area (float): area of plot

       Returns:
            name

       db_table:
            analyses_results_analysis

    """
    #name = models.ForeignKey('Analysis',models.DO_NOTHING, db_column='anaid', blank=False, null=False)
    name = models.CharField(max_length=50,null=False,blank=False)
    parent = TreeForeignKey('results_position',on_delete=models.CASCADE, null=True, blank=True, related_name='analyses')
    xyd = models.CharField(max_length=50,default="",null=True)
    Path = models.CharField(max_length=50,default="",null=True)
    Title = models.CharField(max_length=50,default="",null=True)
    Type = models.CharField(max_length=50,default="",null=True)
    XLabel = models.CharField(max_length=50,default="",null=True)
    YLabel = models.CharField(max_length=50,default="",null=True)
    ScaledBy = models.FloatField(default=1,null=True)
    PolyMarker = models.CharField(max_length=50,default="",null=True)
    ErrorBars = models.CharField(max_length=50,default="",null=True)
    LineColor = models.CharField(max_length=50,default="",null=True)
    yodamerge_scale = models.CharField(max_length=50,default="",null=True)
    mean = models.FloatField(default=0,null=True)
    area = models.FloatField(default=0,null=True)

    def __str__(self):
        return self.name

class scatter3_data(models.Model):
    """
       Contains definition of scatter3_data model:

       Child of results_analyses record

       Parameters:
       parent ('results_analyses'): results analyses parent to this data
                        [This is a tree foreign key link to the 'results_analyses' field]
       Float values from YODA data:
       xval,xerr-,xerr+,yval,yerr-,yerr+,zval,zerr-,zerr+

       db_table:
            analyses_scatter3_data

    """
    parent = models.ForeignKey('results_analyses', models.DO_NOTHING, db_column='results_link', blank=False, null=False)
    xval = models.FloatField(null=True)
    xerr_n = models.FloatField(null=True)
    xerr_p = models.FloatField(null=True)
    yval = models.FloatField(null=True)
    yerr_n = models.FloatField(null=True)
    yerr_p = models.FloatField(null=True)
    zval = models.FloatField(null=True)
    zerr_n = models.FloatField(null=True)
    zerr_p = models.FloatField(null=True)

class scatter2_data(models.Model):
    """
       Contains definition of scatter2_data model:

       Child of results_analyses record

       Parameters:
       parent ('results_analyses'): results analyses parent to this data
                        [This is a tree foreign key link to the 'results_analyses' field]
       Float values from YODA data:
       xval,xerr-,xerr+,yval,yerr-,yerr+

       db_table:
            analyses_scatter2_data

    """
    parent = models.ForeignKey('results_analyses', models.DO_NOTHING, db_column='results_link', blank=False, null=False)
    xval = models.FloatField(null=True)
    xerr_n = models.FloatField(null=True)
    xerr_p = models.FloatField(null=True)
    yval = models.FloatField(null=True)
    yerr_n = models.FloatField(null=True)
    yerr_p = models.FloatField(null=True)


class scatter1_data(models.Model):
    """
       Contains definition of scatter1_data model:

       Child of results_analyses record

       Parameters:
       parent ('results_analyses'): results analyses parent to this data
                        [This is a tree foreign key link to the 'results_analyses' field]
       Float values from YODA data:
       xval,xerr-,xerr+

       db_table:
            analyses_scatter1_data

    """
    parent = models.ForeignKey('results_analyses', models.DO_NOTHING, db_column='results_link', blank=False, null=False)
    xval = models.FloatField(null=True)
    xerr_n = models.FloatField(null=True)
    xerr_p = models.FloatField(null=True)



class histo1_data(models.Model):
    """
       Contains definition of histo1_data model:

       Child of results_analyses record

       Parameters:
       parent ('results_analyses'): results analyses parent to this data
                        [This is a tree foreign key link to the 'results_analyses' field]

       Float values from YODA data:
       xlow,xhigh,sumw,sumw2,sumwx,sumwx2
       Integer values from YODA data:
       numEntries

       db_table:
            analyses_histo1_data

    """
    parent = models.ForeignKey('results_analyses', models.DO_NOTHING, db_column='results_link', blank=False, null=False)
    xlow = models.FloatField(null=True)
    xhigh = models.FloatField(null=True)
    sumw = models.FloatField(null=True)
    sumw2 = models.FloatField(null=True)
    sumwx = models.FloatField(null=True)
    sumwx2 = models.FloatField(null=True)
    numEntries = models.IntegerField(null=True)


class profile1_data(models.Model):
    """
       Contains definition of profile1_data model:

       Child of results_analyses record

       Parameters:
       parent ('results_analyses'): results analyses parent to this data
                        [This is a tree foreign key link to the 'results_analyses' field]

       Float values from YODA data:
       xlow,xhigh,sumw,sumw2,sumwx,sumwx2,sumwy,sumwy2
       Integer values from YODA data:
       numEntries

       db_table:
            analyses_profile1_data

    """
    parent = models.ForeignKey('results_analyses', models.DO_NOTHING, db_column='results_link', blank=False, null=False)
    xlow = models.FloatField(null=True)
    xhigh = models.FloatField(null=True)
    sumw = models.FloatField(null=True)
    sumw2 = models.FloatField(null=True)
    sumwx = models.FloatField(null=True)
    sumwx2 = models.FloatField(null=True)
    sumwy = models.FloatField(null=True)
    sumwy2 = models.FloatField(null=True)
    numEntries = models.IntegerField(null=True)


class overflow_underflow_profile(models.Model):
    """
       Contains definition of overflow_underflow_profile model:

       Child of results_analyses record

       Parameters:
       parent ('results_analyses'): results analyses parent to this data
                        [This is a tree foreign key link to the 'results_analyses' field]

       String values from YODA data:
       row_type (e.g. Total, Overflow, Underflow)
       Float values from YODA data:
       sumw,sumw2,sumwx,sumwx2,sumwy,sumwy2
       Integer values from YODA data:
       numEntries

       db_table:
            analyses_overflow_underflow_profile

    """
    parent = models.ForeignKey('results_analyses', models.DO_NOTHING, db_column='results_link', blank=False, null=False)
    row_type = models.CharField(max_length=50)
    sumw = models.FloatField(null=True)
    sumw2 = models.FloatField(null=True)
    sumwx = models.FloatField(null=True)
    sumwx2 = models.FloatField(null=True)
    sumwy = models.FloatField(null=True)
    sumwy2 = models.FloatField(null=True)
    numEntries  = models.IntegerField(null=True)


class overflow_underflow_histo(models.Model):
    """
       Contains definition of overflow_underflow_histo model:

       Child of results_analyses record

       Parameters:
       parent ('results_analyses'): results analyses parent to this data
                        [This is a tree foreign key link to the 'results_analyses' field]

       String values from YODA data:
       row_type (e.g. Total, Overflow, Underflow)
       Float values from YODA data:
       sumw,sumw2,sumwx,sumwx2
       Integer values from YODA data:
       numEntries

       db_table:
            analyses_overflow_underflow_histo

    """
    parent = models.ForeignKey('results_analyses', models.DO_NOTHING, db_column='results_link', blank=False, null=False)
    row_type = models.CharField(max_length=50)
    sumw = models.FloatField(null=True)
    sumw2 = models.FloatField(null=True)
    sumwx = models.FloatField(null=True)
    sumwx2 = models.FloatField(null=True)
    numEntries = models.IntegerField(null=True)


class counter(models.Model):
    """
       Contains definition of counter model:

       Child of results_analyses record

       Parameters:
       parent ('results_analyses'): results analyses parent to this data
                        [This is a tree foreign key link to the 'results_analyses' field]

       Float values from YODA data:
       sumw,sumw2
       Integer values from YODA data:
       numEntries

       db_table:
            analyses_counter

    """
    parent = models.ForeignKey('results_analyses', models.DO_NOTHING, db_column='results_link', blank=False, null=False)
    sumw = models.FloatField(null=True)
    sumw2 = models.FloatField(null=True)
    numEntries = models.IntegerField(null=True)


class map_header(MPTTModel):
    """
       Contains definition of map_header MPTTmodel:
            This is the header of all .map file data for results


       map_header is parent to:
            - map_pickle

       Parameters:
       ID (int): [Primary Key]
       name (str): Position (also name of yoda file)
       parent ('results_header'): results header parent to this map header
                        [This is a tree foreign key link to the 'results_header' field]
       analyses (str): name of .map file

       Returns:
            ID

       db_table:
            analyses_map_header

    """
    parent = TreeForeignKey('results_header', on_delete=models.CASCADE, null=True, blank=True, related_name='map')
    analyses = models.CharField(max_length=50)

    def __str__(self):
        return self.analyses


class map_pickle(models.Model):
    """
       Contains definition of map_pickle model:
            This is the header of all .map file data for results


       map_pickle is child of map_header

       Parameters:
       ID (int): [Primary Key]
       parent ('results_header'): results header parent to this map header
                        [This is a foreign key link to the 'results_header' field]
       pickle (PickleObject): Field to store pickle object in database

       Returns:
            ID

       db_table:
            analyses_map_header

    """
    parent = models.ForeignKey('map_header',models.DO_NOTHING, db_column='map_header', blank=False, null=False)
    pickle = PickledObjectField()

    def __str__(self):
        return self._check_id_field


def get_dat_path(instance, filename):
    """
       Function to dynamical set path of dat FileField

       Parameters:
           instance: instance of FileField model
           filename (str): name of File


       Returns:
            (str) Path to plots folder

    """
    return "dat_store/" + str(instance.parent.id) + "/data/plots/" + filename.split('/')[-1]

def get_sum_path(instance, filename):
    """
       Function to dynamical set path of summary text FileField

       Parameters:
           instance: instance of FileField model
           filename (str): name of File


       Returns:
            (str) Path to ANALYSIS folder

    """
    return "dat_store/" + str(instance.parent.id) + "/data/ANALYSIS/" + filename.split('/')[-1]

class dat_database(models.Model):
    """
       Contains definition of dat_database model:
            This is the header of all dat file data for results


       dat_database is linked to:
       - summary_text model
       - dat_files model

       Parameters:
       ID (int): [Primary Key]
       parent ('results_position'): results position parent to this map header
                        [This is a foreign key link to the 'results_position' field]
       uploaded (DateTime): time created

       Returns:
            ID

       db_table:
            analyses_dat_database

    """
    results_object = models.ForeignKey('results_position',models.DO_NOTHING, db_column='results_position',
                                       blank=False, null=False)
    uploaded = models.DateField()

    def __str__(self):
        return self._check_id_field

class summary_text(models.Model):
    """
       Contains definition of summary_text model:
            Contains model to store summary.txt file

       Parameters:
       ID (int): [Primary Key]
       parent ('dat_database'): dat header parent to this summary_text model
                        [This is a foreign key link to the 'dat_database' field]
       summary_store (FileField): Summary.txt file

       Returns:
            ID

       db_table:
            analyses_summary_text

    """
    parent = models.ForeignKey('dat_database',models.DO_NOTHING, db_column='dat_database',
                                       blank=False, null=False)
    summary_store = models.FileField(upload_to=get_sum_path)

    def __str__(self):
        return self._check_id_field

class dat_files(models.Model):
    """
       Contains definition of dat_files model:
            Contains model to store .dat files


       Parameters:
       ID (int): [Primary Key]
       name (str): name of .dat file
       parent ('dat_database'): dat header parent to this summary_text model
                        [This is a foreign key link to the 'dat_database' field]
       dat_store (FileField): .dat file

       Returns:
            ID

       db_table:
            analyses_dat_files

    """

    name = models.TextField()
    parent = models.ForeignKey('dat_database',models.DO_NOTHING, db_column='dat_database',
                                       blank=False, null=False)
    dat_store = models.FileField(upload_to=get_dat_path)

    def __str__(self):
        return self._check_id_field

def get_histo_path(instance, filename):
    """
      Function to dynamical set path of histogram FileField

      Parameters:
          instance: instance of FileField model
          filename (str): name of File


      Returns:
           (str) Path to htmlplots folder

   """
    return "dat_store/" + str(instance.id) + "/htmlplots/index.html"

class histo_header(models.Model):
    """
       Contains definition of histo_header model:
            Header for histogram data


       Parameters:
       ID (int): [Primary Key]
       parent ('results_header'): results_header of histogram header
                        [This is a foreign key link to the 'results_position' field]
       uploaded (DateTime): Time of creation

       Returns:
            ID

       db_table:
            analyses_histo_header

    """
    results_object = models.ForeignKey('results_position', models.DO_NOTHING, db_column='results_header',
                                       blank=False, null=False)
    uploaded = models.FileField(upload_to=get_histo_path)

    def __str__(self):
        return self._check_id_field

def get_data_path(instance,filename):
    """
      Function to dynamical set path of histogram data FileField and ImageField

      Parameters:
          instance: instance of FileField/ImageField model
          filename (str): name of File


      Returns:
           (str) Path to htmlplots folder

   """
    if "index" not in filename:
        analysis_folder = str(instance.position.split(".")[0]).split("_")
        folder = ""
        for i in range(len(analysis_folder)-1):
            folder = folder + "_" + analysis_folder[i]
        return "dat_store/" + str(instance.parent.id) + "/htmlplots/" + folder[1:] + "/" + filename
    else:
        folder = instance.position
        return "dat_store/" + str(instance.parent.id) + "/htmlplots/" + folder + "/" + filename

class histo_data(models.Model):
    """
       Contains definition of histo_data model:
            Contains all histogram pdfs and htmls

       Parameters:
       ID (int): [Primary Key]

       parent ('histo_header'): dat header parent to this summary_text model
                        [This is a foreign key link to the 'histo_header' field]
       position (str): Analyses and pattern of data
       dat_store (FileField): html or pdf file

       Returns:
            ID

       db_table:
            analyses_histo_data

    """
    parent = models.ForeignKey('histo_header', models.DO_NOTHING, db_column='histo_header',
                                       blank=False, null=False)
    position = models.CharField(max_length=100)
    dat_store = models.FileField(upload_to=get_data_path)

    def __str__(self):
        return self._check_id_field

class histo_images(models.Model):
    """
       Contains definition of histo_images model:
            Contains all histogram pngs

       Parameters:
       ID (int): [Primary Key]

       parent ('histo_header'): dat header parent to this summary_text model
                        [This is a foreign key link to the 'histo_header' field]
       position (str): Analyses and pattern of data
       dat_store (ImageField): png file

       Returns:
            ID

       db_table:
            analyses_histo_data

    """
    parent = models.ForeignKey('histo_header', models.DO_NOTHING, db_column='histo_header',
                                       blank=False, null=False)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_data_path)

    def __str__(self):
        return self._check_id_field


class attached_files(models.Model):
    """
           Contains definition of attached_files model:
                Contains all extra files linked to positions

           Parameters:
           name ('str'): [Primary Key]

           position ('results_header'): related results header
                            [This is a foreign key link to the 'analyses_header' field]
           file (str): FileField

           Returns:
                name

           db_table:
                analyses_attached_file
    """
    name = models.CharField(primary_key=True,max_length=100)
    parent = models.ForeignKey('results_header', models.DO_NOTHING, db_column='results_header',
                               blank=False, null=False)
    file = models.FileField()

    def __str__(self):
        return self.name


class attached_papers(models.Model):
    """
           Contains definition of attached_files model:
                Contains all extra files linked to positions

           Parameters:

           name ('str'): [Primary Key]
           position ('results_header'): related results header
                            [This is a foreign key link to the 'analyses_header' field]
           file (str): FileField

           Returns:
                name

           db_table:
                analyses_attached_file
    """
    name = models.CharField(primary_key=True,max_length=100)
    parent = models.ForeignKey('results_header', models.DO_NOTHING, db_column='results_header',
                               blank=False, null=False)
    file = models.FileField()

    def __str__(self):
        return self.name
