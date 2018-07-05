# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import Analysis, AnalysisPool,\
                BSM_Model, Used_analyses, Document, Keyword, Linked_keys,\
                runcard, results_header, results_position, results_analyses, \
                scatter3_data,scatter2_data,scatter1_data,histo1_data,\
                profile1_data,overflow_underflow_histo,overflow_underflow_profile,\
                counter

# Register models with import-export instead of basic django functionality


@admin.register(Analysis)
class AnalysisAdmin(ImportExportModelAdmin):
    pass

@admin.register(AnalysisPool)
class AnalysisPoolAdmin(ImportExportModelAdmin):
    pass

@admin.register(BSM_Model)
class BSM_ModelAdmin(ImportExportModelAdmin):
    pass

@admin.register(Used_analyses)
class Used_analysesAdmin(ImportExportModelAdmin):
    pass

@admin.register(Linked_keys)
class Linked_keysAdmin(ImportExportModelAdmin):
    pass

@admin.register(Keyword)
class KeywordAdmin(ImportExportModelAdmin):
    pass

@admin.register(runcard)
class RuncardAdmin(ImportExportModelAdmin):
    pass

@admin.register(results_header)
class ResultsAdmin(ImportExportModelAdmin):
    pass


# Register ImportExport model admin for results tree structure
@admin.register(results_position)
class ResultPositionAdmin(ImportExportModelAdmin):
    pass

@admin.register(results_analyses)
class ResultAnalysesAdmin(ImportExportModelAdmin):
    pass

@admin.register(scatter3_data)
class Scatter3Admin(ImportExportModelAdmin):
    pass

@admin.register(scatter2_data)
class Scatter2Admin(ImportExportModelAdmin):
    pass

@admin.register(scatter1_data)
class Scatter1Admin(ImportExportModelAdmin):
    pass

@admin.register(histo1_data)
class Histo1Admin(ImportExportModelAdmin):
    pass

@admin.register(profile1_data)
class Profile1Admin(ImportExportModelAdmin):
    pass

@admin.register(overflow_underflow_histo)
class OverUnderAdminHisto(ImportExportModelAdmin):
    pass

@admin.register(overflow_underflow_profile)
class OverUnderAdminProfile(ImportExportModelAdmin):
    pass

@admin.register(counter)
class counterAdmin(ImportExportModelAdmin):
    pass