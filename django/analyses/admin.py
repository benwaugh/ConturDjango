# Admin.py: This contains the admin classes for each model.
# Admin classes allow records to be added at app/admin
# ImportExportModelAdmin is used instead of vanilla admin class: This allows for multiple uploads/downloads for admin

from __future__ import unicode_literals

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import Analysis, AnalysisPool,\
                BSM_Model, used_analyses, Document, Keyword, Linked_keys,\
                runcard, results_header, results_position, results_analyses, \
                scatter3_data,scatter2_data,scatter1_data,histo1_data,\
                profile1_data,overflow_underflow_histo,overflow_underflow_profile,\
                counter, ana_file, ana_list, attached_papers, attached_files,\
                histo_images, histo_data,histo_header, dat_files,summary_text,\
                dat_database,map_pickle,map_header

@admin.register(map_header)
class MapHeaderAdmin(ImportExportModelAdmin):
    pass

@admin.register(map_pickle)
class MapPickleAdmin(ImportExportModelAdmin):
    pass

@admin.register(dat_database)
class DatDatabaseAdmin(ImportExportModelAdmin):
    pass

@admin.register(summary_text)
class SummaryTextAdmin(ImportExportModelAdmin):
    pass

@admin.register(dat_files)
class DatFilesAdmin(ImportExportModelAdmin):
    pass

@admin.register(histo_header)
class HistoHeaderAdmin(ImportExportModelAdmin):
    pass

@admin.register(histo_images)
class HistoImagesAdmin(ImportExportModelAdmin):
    pass

@admin.register(histo_data)
class HistoDataAdmin(ImportExportModelAdmin):
    pass

@admin.register(attached_files)
class AttachedFilesAdmin(ImportExportModelAdmin):
    pass

@admin.register(attached_papers)
class AttachedPapersAdmin(ImportExportModelAdmin):
    pass


@admin.register(Analysis)
class AnalysisAdmin(ImportExportModelAdmin):
    pass

@admin.register(AnalysisPool)
class AnalysisPoolAdmin(ImportExportModelAdmin):
    pass

@admin.register(BSM_Model)
class BSM_ModelAdmin(ImportExportModelAdmin):
    pass

@admin.register(used_analyses)
class used_analysesAdmin(ImportExportModelAdmin):
    pass

@admin.register(ana_file)
class ana_fileAdmin(ImportExportModelAdmin):
    pass

@admin.register(ana_list)
class ana_listAdmin(ImportExportModelAdmin):
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