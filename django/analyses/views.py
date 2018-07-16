# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from import_export import resources
from tablib import Dataset
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
import pandas as pd
import json
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import mpld3

# Create your views here.

from .models import Analysis, AnalysisPool,\
                BSM_Model, Used_analyses, Document, Keyword, Linked_keys,\
                runcard, results_header, map_header, map_pickle

from .forms import DocumentForm, DownloadForm


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

def retrieve_file_data(ana_file):
    data_set = Used_analyses.objects.all().filter(modelname=ana_file)
    data = data_set.values('anaid')
    f = open(str(ana_file) + ".ana","w+")
    for line in data:
            f.write("insert Rivet:Analyses 0 " + str(line['anaid']) + "\n")

def model_form_download(request):
    answer = ''
    if request.method == 'POST':
        form = DownloadForm(request.POST, request.FILES)
        answer = form['Model'].value()
    else:
        form = DownloadForm()
    return render(request, 'analyses/model_form_download.html', {
        'form': form
    })

def upload_keywords(request):
    with open('analyses/result.json') as f:
        data = json.load(f)

    for analyses in data:
        if 'cms' in analyses.lower() or 'atlas' in analyses.lower():
            for keywords in data[analyses]['keywords']:
                if Analysis.objects.filter(anaid=analyses).count() > 0:
                    upload_ana,create_ana = Analysis.objects.get_or_create(anaid=str(analyses))
                    upload_kw,create_kw = Keyword.objects.get_or_create(key_word=str(keywords).replace(" ","_"))
                    upload_linked,created_linked = Linked_keys.objects.get_or_create(anaid=upload_ana,key_word=upload_kw)
    return redirect('index')


def store_file_data():
    try:
        dirlist = os.listdir("analyses/temp/")
    except(FileNotFoundError):
        dirlist = []
    if len(dirlist) > 0:
        for filename in dirlist:
            import_dataframe = pd.read_csv("analyses/temp/" + filename)
            columns = list(import_dataframe.columns.values)
            # Automatically categorise file into correct database

            # Analysis Pool Upload
            if 'pool' in columns:
                pools_list = import_dataframe['pool']
                ana_list = import_dataframe['anaid']
                lumi_list = import_dataframe['lumi']
                i = 0
                for ana in ana_list:
                    upload_pool,create_p = AnalysisPool.objects.get_or_create(pool=pools_list[i])
                    upload_ana,create_a = Analysis.objects.get_or_create(anaid=ana,pool=upload_pool,lumi=lumi_list[i])
                    upload_ana.save()
                    upload_pool.save()
                    i =+ 1

            # Model Upload
            if 'name' in columns:
                ana_list = import_dataframe['anaid']
                bsm_list = import_dataframe['name']
                i = 0
                for ana in ana_list:
                    upload_ana,create_a = Analysis.objects.get_or_create(anaid=ana)
                    upload_bsm,create_b = BSM_Model.objects.get_or_create(name=bsm_list[i])
                    upload_used,create_u = Used_analyses.objects.get_or_create(anaid=upload_ana,modelname=upload_bsm)
                    upload_bsm.save()
                    upload_used.save()
                    upload_ana.save()
                    i =+ 1
            os.remove("analyses/temp/" + filename)
        os.rmdir("analyses/temp")

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DocumentForm()

    store_file_data()
    return render(request, 'analyses/model_form_upload.html', {
        'form': form
    })

def index(request):
    analysis_pools = AnalysisPool.objects.order_by('pool')
    analysis_list = Analysis.objects.order_by('anaid')
    models_list = BSM_Model.objects.order_by('name')
    keywords_list = Keyword.objects.order_by('key_word')
    runcard_list = runcard.objects.order_by('runcard_name')
    results_list = results_header.objects.order_by('name')
    context = {
        'analysis_pools' : analysis_pools,
        'analysis_list' : analysis_list,
        'models_list' : models_list,
        'keywords_list': keywords_list,
        'runcard_list':runcard_list,
        'results_list':results_list
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

def Runcard(request, runcard_name):
    r = get_object_or_404(runcard, pk=runcard_name)
    context = {
        'rc' : r,
    }
    return render(request, 'analyses/runcard.html', context)

def blacklists(request, anaid):
    return HttpResponse("You're looking at blacklists for %s." % anaid)

def keywords_list(request, key_word):
    k = get_object_or_404(Keyword, pk=key_word)
    context = {
        'key' : k,
    }
    return render(request, 'analyses/key_word.html', context)

def results(request, name):
    n = get_object_or_404(results_header, pk=name)
    map_h = map_header.objects.filter(parent=n)
    context = {
        'res' : n,
        'mh':map_h[0],
    }
    return render(request, 'analyses/results.html', context)

def heatmap_display(request, analyses):
    file = get_object_or_404(map_header, pk=analyses)
    data = map_pickle.objects.filter(parent=file.tree_id).values_list('pickle',flat=True)

    import mpld3
    from .management.commands.generate_heatmap import gen_heatmap

    mpl_figure = plt.figure(1, figsize=(6, 6))

    fig_html = gen_heatmap(data)

    context = {
        'hea' : file,
        'dat': data,
        'figure': fig_html,
    }
    return render(request, 'analyses/heatmap.html', context)

