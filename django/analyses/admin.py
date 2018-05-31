# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import Analysis, AnalysisPool, BSM_Model, Used_analyses

#admin.site.register(Analysis)
#admin.site.register(AnalysisPool)
#admin.site.register(BSM_Model)
#admin.site.register(Used_analyses)
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
