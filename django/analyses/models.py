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



