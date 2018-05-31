# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from import_export import resources
from tablib import Dataset
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.

from .models import Analysis, AnalysisPool, BSM_Model, Used_analyses, Document
from .forms import DocumentForm



class export_resource(resources.ModelResource):
    class Meta:
        model = Used_analyses
        fields = ('anaid',)

class Used_resource(resources.ModelResource):
    class Meta:
        model = Used_analyses

class Ana_resource(resources.ModelResource):
    class Meta:
        model = Analysis

class Pool_resource(resources.ModelResource):
    class Meta:
        model = AnalysisPool

class BSM_resource(resources.ModelResource):
    class Meta:
        model = BSM_Model


def export(mod_name):
    ana_resource = export_resource()
    filtered =  Used_analyses.objects.filter(modelname=mod_name)
    dataset = ana_resource.export(filtered)
    return dataset.csv

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })

def index(request):
    analysis_pools = AnalysisPool.objects.order_by('pool')
    analysis_list = Analysis.objects.order_by('anaid')
    models_list = BSM_Model.objects.order_by('name')
    context = {
        'analysis_pools' : analysis_pools,
        'analysis_list' : analysis_list,
        'models_list' : models_list,
    }
    return render(request, 'analyses/index.html',context)

def pool(request, pool):
    p = get_object_or_404(AnalysisPool, pk=pool)
    context = {
        'pool' : p,
    }
    return render(request, 'analyses/pool.html', context)

def analysis(request, anaid):
    a = get_object_or_404(Analysis, pk=anaid)
    context = {
        'ana' : a,
    }
    return render(request, 'analyses/analysis.html', context)

def model(request, name):
    m = get_object_or_404(BSM_Model, pk=name)
    context = {
        'mod' : m,
    }
    return render(request, 'analyses/model.html', context)

def blacklists(request, anaid):
    return HttpResponse("You're looking at blacklists for %s." % anaid)
