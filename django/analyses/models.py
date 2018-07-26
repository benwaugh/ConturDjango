# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from mptt.models import MPTTModel, TreeForeignKey
from picklefield.fields import PickledObjectField



@python_2_unicode_compatible
class Analysis(models.Model):
    anaid = models.TextField(primary_key=True)
    lumi = models.FloatField()
    pool = models.ForeignKey('AnalysisPool', models.DO_NOTHING, db_column='pool', blank=True, null=True)
    def __str__(self):
        return self.anaid

    class Meta:
        db_table = 'analysis'



@python_2_unicode_compatible
class AnalysisPool(models.Model):
    pool = models.TextField(primary_key=True)
    def __str__(self):
        return self.pool

    class Meta:
        db_table = 'analysis_pool'



@python_2_unicode_compatible
class Blacklist(models.Model):
    anaid = models.ForeignKey(Analysis, models.DO_NOTHING, db_column='anaid')
    pattern = models.TextField()
    def __str__(self):
        return '%s %s' % (self.anaid, self.pattern)

    class Meta:
        db_table = 'blacklist'



@python_2_unicode_compatible
class Normalization(models.Model):
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
    anaid = models.ForeignKey(Analysis, models.DO_NOTHING, db_column='anaid')
    pattern = models.TextField()
    def __str__(self):
        return '%s %s' % (self.anaid, self.pattern)

    class Meta:
        db_table = 'whitelist'



@python_2_unicode_compatible
class BSM_Model(models.Model):
    name = models.TextField(primary_key=True)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bsm_model'



@python_2_unicode_compatible
class Used_analyses(models.Model):
    modelname = models.ForeignKey('BSM_Model', models.DO_NOTHING, db_column='name', blank=False, null=False)
    anaid = models.ForeignKey('Analysis', models.DO_NOTHING, db_column='anaid', blank=False, null=False)
    def __str__(self):
        return '%s %s' % (self.modelname, self.anaid)

    class Meta:
        db_table = 'used_analyses'
        unique_together = (('modelname', 'anaid'),)



@python_2_unicode_compatible
class Download(models.Model):
    now = datetime.datetime.now()
    runcard_name = models.CharField(max_length=200, default=now.strftime("%d%m%Y%H%M"),primary_key=True)
    FILE_CHOICES = zip(BSM_Model.objects.all().values_list('name', flat=True) [0::1], BSM_Model.objects.all().values_list('name', flat=True)[0::1])
    Model = models.CharField(max_length=200, choices=FILE_CHOICES, default='')
    Parameter_Card = models.FileField(upload_to='analyses/parameters-cards/', default='')



@python_2_unicode_compatible
class Document(models.Model):
    UPLOAD_CHOICES = (
    ('Analyses','Analyses'),
    ('Analyses_Pool', 'Analyses Pool'),
    ('BSM_Model','BSM Model'),
    )
    upload_type = models.CharField(max_length=20, choices=UPLOAD_CHOICES, default='Analyses')
    upload_file = models.FileField(upload_to='analyses/temp/',default='')
    uploaded_at = models.DateTimeField(auto_now_add=True)



@python_2_unicode_compatible
class Keyword(models.Model):
    key_word = models.TextField(primary_key=True)

    def __str__(self):
        return self.key_word

    class Meta:
        db_table = 'keywords_list'



@python_2_unicode_compatible
class Linked_keys(models.Model):
    anaid = models.ForeignKey('Analysis', models.DO_NOTHING, db_column='anaid', blank=False, null=False)
    key_word = models.ForeignKey('Keyword', models.DO_NOTHING, db_column='keyword', blank=False, null=False)
    def __str__(self):
        return '%s %s' % (self.key_word, self.anaid)

    class Meta:
        db_table = 'linked_keywords'
        unique_together = (('key_word', 'anaid'),)



@python_2_unicode_compatible
class runcard(models.Model):
    now = datetime.datetime.now()
    runcard_name = models.CharField(max_length=50, default=now.strftime("%d%m%Y%H%M"),primary_key=True)
    modelname = models.ForeignKey('BSM_Model', models.DO_NOTHING, db_column='name', blank=False, null=False)
    param_card = models.FileField(upload_to='analyses/parameters-cards/')
    UFO_model = models.URLField(default="http://feynrules.irmp.ucl.ac.be/")

    def __str__(self):
        return self.runcard_name

    class Meta:
        db_table = 'runcard_export'
        unique_together = (('runcard_name', 'param_card'),)




# Define Modified Preorder Tree Traversal  Structure
class results_header(MPTTModel):
    name = models.CharField(max_length=50, unique=True,primary_key=True)
    runcard = models.ForeignKey('runcard', models.DO_NOTHING, db_column='runcard_name', blank=False, null=False,default='')
    mc_ver = models.CharField(max_length=20, default='0.0.0')
    contur_ver = models.CharField(max_length=20, default='0.0.0')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='results')

    class MPTTMeta:
        order_insertion_by = ['name']



class results_position(MPTTModel):
    name = models.CharField(max_length=50,unique=False)
    parent = TreeForeignKey('results_header', on_delete=models.CASCADE, null=False, blank=True, related_name='position')

    class MPTTMeta:
        order_insertion_by = ['name']



class results_analyses(MPTTModel):

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


class scatter3_data(models.Model):
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
    parent = models.ForeignKey('results_analyses', models.DO_NOTHING, db_column='results_link', blank=False, null=False)
    xval = models.FloatField(null=True)
    xerr_n = models.FloatField(null=True)
    xerr_p = models.FloatField(null=True)
    yval = models.FloatField(null=True)
    yerr_n = models.FloatField(null=True)
    yerr_p = models.FloatField(null=True)


class scatter1_data(models.Model):
    parent = models.ForeignKey('results_analyses', models.DO_NOTHING, db_column='results_link', blank=False, null=False)
    xval = models.FloatField(null=True)
    xerr_n = models.FloatField(null=True)
    xerr_p = models.FloatField(null=True)



class histo1_data(models.Model):
    parent = models.ForeignKey('results_analyses', models.DO_NOTHING, db_column='results_link', blank=False, null=False)
    xlow = models.FloatField(null=True)
    xhigh = models.FloatField(null=True)
    sumw = models.FloatField(null=True)
    sumw2 = models.FloatField(null=True)
    sumwx = models.FloatField(null=True)
    sumwx2 = models.FloatField(null=True)
    numEntries = models.IntegerField(null=True)


class profile1_data(models.Model):
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
    parent = models.ForeignKey('results_analyses', models.DO_NOTHING, db_column='results_link', blank=False, null=False)
    row_type = models.CharField(max_length=50)
    sumw = models.FloatField(null=True)
    sumw2 = models.FloatField(null=True)
    sumwx = models.FloatField(null=True)
    sumwx2 = models.FloatField(null=True)
    numEntries = models.IntegerField(null=True)


class counter(models.Model):
    parent = models.ForeignKey('results_analyses', models.DO_NOTHING, db_column='results_link', blank=False, null=False)
    sumw = models.FloatField(null=True)
    sumw2 = models.FloatField(null=True)
    numEntries = models.IntegerField(null=True)


class map_header(MPTTModel):
    parent = TreeForeignKey('results_header', on_delete=models.CASCADE, null=True, blank=True, related_name='map')
    analyses = models.CharField(max_length=50,primary_key=True)


class map_data(models.Model):
    parent = models.ForeignKey('map_header',models.DO_NOTHING, db_column='map_header', blank=False, null=False)
    model_position = models.IntegerField(null=True)
    meas = models.FloatField(null=True)
    bg = models.FloatField(null=True)
    sErr = models.FloatField(null=True)
    measErr = models.FloatField(null=True)
    s = models.FloatField(null=True)
    bgErr = models.FloatField(null=True)
    kev = models.FloatField(null=True)
    isRatio = models.BooleanField()


class map_pickle(models.Model):
    parent = models.ForeignKey('map_header',models.DO_NOTHING, db_column='map_pickle', blank=False, null=False)
    pickle = PickledObjectField()


class ufo_objects(models.Model):
    name = models.TextField()
    download_location = models.TextField()
    date_downloaded = models.DateField()


class dat_database(models.Model):
    results_object = models.ForeignKey('results_header',models.DO_NOTHING, db_column='results_header',
                                       blank=False, null=False)
    uploaded = models.DateField()


class contur_plots(models.Model):
    results_object = models.ForeignKey('results_header', models.DO_NOTHING, db_column='results_header',
                                       blank=False, null=False)
    uploaded = models.DateField()

