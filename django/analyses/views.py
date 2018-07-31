# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from import_export import resources
from tablib import Dataset
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import glob, os, sys
import pandas as pd
import json
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import mpld3
from datetime import datetime
import wget
import tarfile
from django.template import Template, Context
from django.views.generic.base import TemplateView
import os
import zipfile

from .models import Analysis, AnalysisPool,\
                BSM_Model, used_analyses, Document, Keyword, Linked_keys,\
                runcard, results_header, map_header, map_pickle, results_position,\
                results_analyses,counter,scatter1_data,scatter2_data,scatter3_data,\
                histo1_data,profile1_data,overflow_underflow_profile,\
                overflow_underflow_histo, contur_plots, ana_file, ana_list

from .forms import DocumentForm, DownloadForm,UFOForm


#class export_resource(resources.ModelResource):
#    class Meta:
#        model = Used_analyses
#        fields = ('anaid',)

#class Used_resource(resources.ModelResource):
#    class Meta:
#        model = Used_analyses

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
    a = 1
    #data_set = Used_analyses.objects.all().filter(modelname=ana_file)
    #data = data_set.values('anaid')
    #f = open(str(ana_file) + ".ana","w+")
    #for line in data:
    #        f.write("insert Rivet:Analyses 0 " + str(line['anaid']) + "\n")

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
                    upload_used,create_u = ana_file.objects.get_or_create(anaid=upload_ana,modelname=upload_bsm)
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
    #results_list = results_header.objects.order_by('name')
    histo_list = results_header.objects.filter(type="Histogram").order_by('name')
    heatmap_list = results_header.objects.filter(type="Heatmap").order_by('name')
    context = {
        'analysis_pools' : analysis_pools,
        'analysis_list' : analysis_list,
        'models_list' : models_list,
        'keywords_list': keywords_list,
        'runcard_list':runcard_list,
        'histo_list':histo_list,
        'heatmap_list': heatmap_list,
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
    linked_ana = used_analyses.objects.filter(modelname=m)
    context = {
        'mod' : m,
        'ana' : linked_ana,
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
    yoda_list = results_position.objects.filter(parent=n)
    plots = contur_plots.objects.filter(results_object=n)
    context = {
        'res' : n,
        'mh':map_h,
        'yoda_list':yoda_list,
        'plots':plots
    }
    return render(request, 'analyses/results.html', context)

def positions(request, id):
    y = get_object_or_404(results_position,pk=id)
    analyses_list = results_analyses.objects.filter(parent=id)
    context = {
        'y':y,
        'ana_list':analyses_list,
    }
    return render(request, 'analyses/positions.html', context)

def ana_data(request, id):
    details = get_object_or_404(results_analyses,pk=id)
    counter_list = counter.objects.filter(parent=id)
    scatter1 = scatter1_data.objects.filter(parent=id)
    scatter2 = scatter2_data.objects.filter(parent=id)
    scatter3 = scatter3_data.objects.filter(parent=id)
    histo1 = histo1_data.objects.filter(parent=id)
    profile1 = profile1_data.objects.filter(parent=id)
    overflow_underflow_histogram = overflow_underflow_histo.objects.filter(parent=id)
    overflow_underflow_prof = overflow_underflow_profile.objects.filter(parent=id)
    context = {
        'details':details,
        'counter_list':counter_list,
        'scatter1':scatter1,
        'scatter2':scatter2,
        'scatter3':scatter3,
        'histo1':histo1,
        'profile1':profile1,
        'ouh':overflow_underflow_histogram,
        'oup':overflow_underflow_prof,
    }
    return render(request, 'analyses/ana_data.html', context)

def heatmap_display(request,analyses):
    file = get_object_or_404(map_header, pk=analyses)
    data = map_pickle.objects.filter(parent=file.tree_id).values_list('pickle',flat=True)
    from .management.commands.generate_heatmap import gen_heatmap
    gen_heatmap(data)
    return redirect(request.META['HTTP_REFERER'])

def ufo_home(request):
    answer = ''
    if request.method == 'POST':
        form = UFOForm(request.POST, request.FILES)
        name = form['name'].value()
        link = form['UFO_Link'].value()
        author = form['author'].value()
        date = datetime.now()
        create_record_and_dl(name,link,date,author)
    else:
        form = UFOForm()
    return render(request, 'analyses/ufo_home.html', {
        'form': form
    })

def create_record_and_dl(name,link,date,author):
    directory = "analyses/modelUFOs/" + name + "/"
    if not os.path.exists(directory):
        os.makedirs(directory)
    ufo_record,ufo_created = BSM_Model.objects.get_or_create(name=name,UFO_Link=link,date_downloaded=date,author=author)
    ufo_record.save()
    wget.download(link,out=directory)

    sys.path.append(os.path.dirname(os.path.dirname(directory)))

    for file in glob.glob(directory + "/*.tgz"):
        print(file)
        tar = tarfile.open(file)
        tar.extractall("analyses/models/" + str(ufo_record.name) + "/")
        tar.close()
        print("here")


def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        print(dirs)
        for file in files:
            ziph.write(os.path.join(root, file))

def download_html(request,id):
    zipf = zipfile.ZipFile(str(id) + '.zip', 'w', zipfile.ZIP_DEFLATED)
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(os.path.dirname(CURRENT_DIR)))

    zipdir(CURRENT_DIR+ '/dat_store/' + id + '/htmlplots/', zipf)
    #print(os.path.dirname(os.path.abspath(__file__)))
    zipf.close()
    return redirect(request.META['HTTP_REFERER'])

def dl_bsm(request,name):
    a = 1

def add_ana(request,name):
    ana_file_list = ana_list.objects.all()
    model = BSM_Model.objects.filter(name=name)
    context = {
        'm': model[0],
        'anas':ana_file_list,
    }
    return render(request, 'analyses/add_ana.html', context)

def ana_file_view(request,name):
    context = {
    }
    return render(request, 'analyses/add_ana.html', context)

def add_existing_ana(request,name,modelname):
    model = BSM_Model.objects.get(name=modelname)
    ana_file = ana_list.objects.get(ana_name=name)
    value,created = used_analyses.objects.get_or_create(modelname=model,ana_name=ana_file)

    ana_file_list = used_analyses.objects.all()
    model = BSM_Model.objects.filter(name=modelname)

    context = {
        'm': model[0],
        'anas': ana_file_list,
    }
    return render(request,'analyses/add_ana.html',context)

def inside_ana(request,ana_name):
    a = 1