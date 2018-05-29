# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Analysis, AnalysisPool, BSM_Model, Used_analyses

admin.site.register(Analysis)

admin.site.register(AnalysisPool)

admin.site.register(BSM_Model)

admin.site.register(Used_analyses)

