# -*- coding: utf-8 -*-

# Views.py: Contains the 'Views' part of the model view template pattern, where functions define what is shown to users
# in templates
# Excluding a few complementary functions, most functions in this file define which data to display to html files as
# they are rendered

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
from django.http import Http404
import matplotlib
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
from wsgiref.util import FileWrapper
from .models import Analysis, AnalysisPool,\
                BSM_Model, used_analyses, Document, Keyword, Linked_keys,\
                runcard, results_header, map_header, map_pickle, results_position,\
                results_analyses,counter,scatter1_data,scatter2_data,scatter3_data,\
                histo1_data,profile1_data,overflow_underflow_profile,\
                overflow_underflow_histo, histo_header, ana_file, ana_list, histo_data, histo_images,\
                attached_papers,attached_files

from .forms import DocumentForm, DownloadForm,UFOForm, AnalysesForm, PoolForm, PaperForm, FilesForm


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
        runcard_name = form['runcard_name'].value()
        modelname = form['modelname'].value()
        BSM_instance = BSM_Model.objects.filter(name=modelname)[0]

        param_card = form['param_card'].value()
        author = form['author'].value()
        runcard_object, runcard_created = runcard.objects.get_or_create(
            runcard_name=runcard_name,modelname=BSM_instance,param_card=param_card,author=author)
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
    """
        Purpose:
            Links document form to model_form_upload template
            This produces the form required to upload a new analysis into the system

        Parameters:
            Web request -> Comes from 'New Analysis' link.
            Has no data specific arguments

        Operations:
            Saves new analysis to database through form

        Context:
            No Specific Context

        Returns:
            Renders Analysis Upload form

    """
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DocumentForm()

    return render(request, 'analyses/model_form_upload.html', {
        'form': form
    })

def pool_form(request):
    """
        Purpose:
            Links pool form to pool_form template
            This produces the form required to upload a new analysis pool into the system

        Parameters:
            Web request -> Comes from 'New Pool' link.
            Has no data specific arguments

        Operations:
            Saves new pool to database through form

        Context:
            No Specific Context

        Returns:
            Renders Pool Upload form

    """
    if request.method == 'POST':
        form = PoolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PoolForm()

    return render(request, 'analyses/pool_form.html', {
        'form': form
    })

def index(request):
    """
        Purpose:
            Renders 'homepage' (index) of CoRaD, containing many different sections of information.

        Parameters:
            Web request -> homepage of CoRaD system.
            Has no data specific arguments

        Operations:
            No calculations undertaken.

        Context:
            Loads all Analysis Pools
            Loads all Analyses
            Loads all Models
            Loads all Keywords
            Loads all Runcards
            Loads all Results

        Returns:
            Renders Index template with context
    """
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
        'results_list':results_list,
    }
    return render(request, 'analyses/index.html',context)

def pool(request, pool):
    """
        Purpose:
            Renders page showing data for a specific pool

        Parameters:
            Web request -> Activated by clicking on a specific pool in index list.
            Pool -> Pool name string taken from link that has been clicked on

        Operations:
            No calculations undertaken.

        Context:
            Get Pool object matching input pool name

        Returns:
            Renders Pool template with corresponding pool data
    """
    p = get_object_or_404(AnalysisPool, pk=pool)
    context = {
        'pool' : p,
    }
    return render(request, 'analyses/pool.html', context)

def analysis(request, anaid):
    """
        Purpose:
            Renders page showing data for analysis

        Parameters:
            Web request -> Activated by clicking on a specific analysis in index list.
            anaid -> anaid name string taken from link that has been clicked on

        Operations:
            No calculations undertaken.

        Context:
            Get Analysis object matching input anaid name

        Returns:
            Renders analysis template with corresponding analysis data
    """
    a = get_object_or_404(Analysis, pk=anaid)
    context = {
        'ana' : a,
    }
    return render(request, 'analyses/analysis.html', context)

def model(request, name):
    """
        Purpose:
            Renders page showing data for model

        Parameters:
            Web request -> Activated by clicking on a specific model in index list.
            name -> model name string taken from link that has been clicked on

        Operations:
            No calculations undertaken.

        Context:
            Get model object matching input model name
            Get all analysis linked to model

        Returns:
            Renders model template with corresponding model and analysis data
    """
    m = get_object_or_404(BSM_Model, pk=name)
    linked_ana = used_analyses.objects.filter(modelname=m)
    context = {
        'mod' : m,
        'ana' : linked_ana,
    }
    return render(request, 'analyses/model.html', context)

def Runcard(request, runcard_name):
    """
        Purpose:
            Renders page showing data for runcard

        Parameters:
            Web request -> Activated by clicking on a specific runcard in index list.
            runcard_name -> runcard name string taken from link that has been clicked on

        Operations:
            No calculations undertaken.

        Context:
            Get runcard object matching input runcard name
            Get model linked to runcard
            Get analyses linked to model

        Returns:
            Renders runcard template with corresponding runcard, model and analysis data
    """
    r = get_object_or_404(runcard, pk=runcard_name)
    m = BSM_Model.objects.filter(name=r.modelname)
    anas = used_analyses.objects.filter(modelname__in=m)
    context = {
        'rc' : r,
        'm':m[0],
        'anas':anas
    }
    return render(request, 'analyses/runcard.html', context)

def blacklists(request, anaid):
    return HttpResponse("You're looking at blacklists for %s." % anaid)

def keywords_list(request, key_word):
    """
        Purpose:
            Renders page showing keyword

        Parameters:
            Web request -> Activated by clicking on a specific keyword in list.
            key_word -> keyword string taken from link that has been clicked on

        Operations:
            No calculations undertaken.

        Context:
            Get keyword object matching input keyword name

        Returns:
            Renders key_word template
    """
    k = get_object_or_404(Keyword, pk=key_word)
    context = {
        'key' : k,
    }
    return render(request, 'analyses/key_word.html', context)

def results(request, name):
    """
        Purpose:
            Renders page showing data for results

        Parameters:
            Web request -> Activated by clicking on a specific results in index list.
            name -> results name string taken from link that has been clicked on

        Operations:
            No calculations undertaken.

        Context:
            Get results object matching input results name
            Get map headers whose parent is results object
            Get yoda files whose parent is results object
            Names of parameters
            Parameters for each record

        Returns:
            Renders results template with corresponding results and plot data
    """
    n = get_object_or_404(results_header, pk=name)
    map_h = map_header.objects.filter(parent=n)
    yoda_list = results_position.objects.filter(parent=n)
    papers = attached_papers.objects.filter(parent=n)
    files = attached_files.objects.filter(parent=n)

    try:
        param1 = str(yoda_list[0].name).split('_')[0]
        param2 = str(yoda_list[0].name).split('_')[2]
    except(IndexError):
        param1 = "param1"
        param2 = "param2"

    for i in range(0,len(yoda_list)):
        try:
                yoda_list[i].param1s=str(yoda_list[i].name).split('_')[1]
                yoda_list[i].param2s =str(yoda_list[i].name).split('_')[3]
        except(IndexError):
                yoda_list[i].param1s = ""
                yoda_list[i].param2s = ""



    context = {
        'res' : n,
        'mh':map_h,
        'yoda_list':yoda_list,
        'p1':param1,
        'p2':param2,
        'papers':papers,
        'files':files,
    }
    return render(request, 'analyses/results.html', context)

def positions(request, id):
    """
        Purpose:
            Renders page showing data for specific results position (combination of parameters)
            (For example mY_100_mX_300 is a position)

        Parameters:
            Web request -> Activated by clicking on a specific results in positions list in results header template.
            id -> unique id of positon

        Operations:
            No calculations undertaken.

        Context:
            Get results position object with corresponding ID
            Get list of analyses and patterns that results position is the parent of

        Returns:
            Renders positions template with corresponding contained analyses patterns
    """
    y = get_object_or_404(results_position,pk=id)
    analyses_list = results_analyses.objects.filter(parent=id)
    histo_head = histo_header.objects.filter(results_object=y)
    histo_list = histo_images.objects.filter(parent__in=histo_head)
    for i in range(0,len(histo_list)):
        data = histo_list[i].position.split(".")[0]
        histo_list[i].pattern = data.split("_")[-1]
        analysis = ""
        for j in range(0,len(data.split("_"))-1):
            analysis = analysis + "_" + data.split("_")[j]
        histo_list[i].analysis = analysis[1:]

    context = {
        'y':y,
        'ana_list':analyses_list,
        'hl':histo_list
    }
    return render(request, 'analyses/positions.html', context)

def ana_data(request, id):
    """
        Purpose:
            Renders page showing all YODA data for an analysis and pattern

        Parameters:
            Web request -> Activated by clicking on a specific analysis and patter in results section.
            id -> unique id of analysis and pattern combination

        Operations:
            No calculations undertaken.

        Context:
            Get results analysis/pattern object with corresponding ID
            Get child data from object using ID:
                - Counter table
                - 1d,2d,3d scatter data
                - 1d histogram data
                - 1d profile data
                - Overflow/Underflow data for profile and histogram

        Returns:
            Renders YODA analysis data template containing each data set that is a child of analysis/pattern object

    """
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
    """
        Purpose:
            Opens new tab that plots heatmap from database

        Parameters:
            Web request -> Activated by clicking on create heatmap link in results page
            analyses -> .map file name to plot

        Operations:
            Loads pickle from map database that matches corresponding parent id
            Calls gen_heatmap (from generate heatmap) python script from commands folder with pickle as argument
            Calls get_heatmap (from histo_view) to get histogram data
            This uses Bokeh to plot the heatmap, and render a table with contributing histogram data

        Context:
            Items: Contains contributing histograms to areas of plots, with data on name, exclusion, and pattern and image data

        Returns:
            Refreshes current page

    """
    file = map_header.objects.get(analyses=analyses)
    data = map_pickle.objects.filter(parent=file.id).values_list('pickle',flat=True)

    header = file.parent

    # Create data structures for use in HTML
    class plots_obj:
        def __init__(self):
            self.plot = ""
            self.pattern = ""

    class datum:
        def __init__(self):
            self.name = ""
            self.cl = 0
            self.plots = []

        def __str__(self):
            return self.name

    from .management.commands.generate_heatmap import gen_heatmap as gh
    from .management.commands.histo_view import gen_heatmap as hv
    gh(data,header)
    plot_list, parameter_table, cls,analyses_table = hv(data,header)


    items = []

    for i in range(0,len(plot_list)):
        item = datum()
        item.cl = cls[i]
        item.name = parameter_table[i]

        plots_list = []
        for j in range(0,len(plot_list[i])):
            plots_input = plots_obj()
            plots_input.plot = plot_list[i][j]
            plots_input.pattern = analyses_table[i][j]
            plots_list.append(plots_input)

        item.plots = plots_list
        items.append(item)


    context = {
        'items': items,
    }
    return render(request, 'analyses/cls_view.html', context)

def ufo_home(request):
    """
        Purpose:
            Create new model using UFO file
            This function creates a new record and downloads the corresponding UFO file from FeynRules

        Parameters:
            Web request -> Activated by clicking on new model link.

        Operations:
            Read data from input form and call create_record_and_dl function

        Context:
            No specific context.

        Returns:
            Renders form and ufo creation template

    """
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
    """
        Purpose:
            Creates new model record from data recieved from ufo_home view, and download model to internal files

        Parameters:
            name (str): name of BSM model
            link (str): Link to raw data download of FeynRules Model
            date (DateTime): time of creation of model
            author (str): name of creator of new model

        Operations:
            Create new directory for zipped UFO file
            Create new record in BSM model database with input parameters
            Download file directly from FeynRules into new internal directory

        Context:
            No specific context.

        Returns:
            None

    """
    directory = "analyses/modelUFOs/" + name + "/"
    if not os.path.exists(directory):
        os.makedirs(directory)
    ufo_record,ufo_created = BSM_Model.objects.get_or_create(name=name,UFO_Link=link,date_downloaded=date,author=author)
    ufo_record.save()
    wget.download(link,out=directory)

def zipdir(path, ziph):
    """
        Purpose:
            Zip existing directory

        Parameters:
            Path (str): Path to directory to be zipped
            ziph (ZippedFile): Zip file object to be created

        Operations:
            Zip all contained files into folder

        Context:
            No specific context.

        Returns:
            None

    """
    for root, dirs, files in os.walk(path):
        print(dirs)
        for file in files:
            ziph.write(os.path.join(root, file))

def download_html(request,id):
    """
        Purpose:
            Downloads directory containing HTML files as zip

        Parameters:
            Web request -> Activated by clicking on export plots link
            id -> results objects unique id

        Operations:
            Zips file using zipdir function

        Context:
            No specific context

        Returns:
            Refreshes current page

    """
    zipf = zipfile.ZipFile(str(id) + '.zip', 'w', zipfile.ZIP_DEFLATED)
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(os.path.dirname(CURRENT_DIR)))

    zipdir(CURRENT_DIR+ '/dat_store/' + id + '/htmlplots/', zipf)
    #print(os.path.dirname(os.path.abspath(__file__)))
    zipf.close()
    return redirect(request.META['HTTP_REFERER'])

def dl_bsm(request,name):
    """
        Purpose:
            Downloads Model files from internal data files

        Parameters:
            Web request -> Activated by clicking on export BSM model link
            name -> BSM model name

        Operations:
            Searches for folder matching BSM model name in directory
            Creates http file wrapper
            Presents download to user

        Context:
            No specific context

        Returns:
            Requests Download to user in standard format

    """
    for file in glob.glob("analyses/modelUFOs/" + name + "/*.tgz"):
        try:
            wrapper = FileWrapper(open(file, 'rb'))
            response = HttpResponse(wrapper, content_type='application/force-download')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file)
            return response
        except Exception as e:
            return None

def add_ana(request,name):
    """
        Purpose:
            Loads screen to add new ana files to a model

        Parameters:
            Web request -> Activated by clicking on add new ana link
            name -> name of BSM model

        Operations:
            No calculations undertaken.

        Context:
            Get all existing ana files
            Get data for current model

        Returns:
            Renders add ana template linked to active model page

    """
    ana_file_list = ana_list.objects.all()
    model = BSM_Model.objects.filter(name=name)

    try:
        model[0]
    except(IndexError):
        raise Http404()

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
    """
        Purpose:
            Link an existing .ana file to a new model

        Parameters:
            Web request -> Activated by clicking on add existing .ana link
            name -> name of ana_file
            modelname -> name of active model

        Operations:
            Create new record in used analyses table with current ana file and model

        Context:
            Get all ana files
            Get active model

        Returns:
            Renders add ana page with new data added

    """
    try:
        model = BSM_Model.objects.get(name=modelname)
        ana_file = ana_list.objects.get(ana_name=name)
        value,created = used_analyses.objects.get_or_create(modelname=model,ana_name=ana_file)

        ana_file_list = used_analyses.objects.all()
        model = BSM_Model.objects.filter(name=modelname)
    except:
        raise Http404()

    try:
        model[0]
    except(IndexError):
        raise Http404()

    context = {
        'm': model[0],
        'anas': ana_file_list,
    }
    return render(request,'analyses/add_ana.html',context)

def inside_ana(request,ana_name):
    """
        Purpose:
            Get information related to a specific ana file

        Parameters:
            Web request -> Activated by clicking on embedded ana file link
            ana_name -> name of .ana file

        Operations:
            No calculations undertaken.

        Context:
            Get .ana file object corresponding to click
            Get all analyses linked to .ana file object

        Returns:
            Renders inside_ana template with analyses and .ana data

    """
    try:
        linked_ana = ana_list.objects.get(ana_name=ana_name)
        ana_file_list = ana_file.objects.filter(linked_ana=linked_ana)
    except:
        raise Http404()
    context = {
        'anas':ana_file_list,
        'n':linked_ana,
    }
    return render(request, 'analyses/inside_ana.html', context)

def new_ana(request,name):
    """
        Purpose:
            Create new ana file by selecting multiple analyses from list

        Parameters:
            Web request -> Activated by clicking on create and link new ana link
            name -> name of BSM model

        Operations:
            Load Analyses form
            Display all Analyses to user
            Determine which Analyses are ticked by user
            For each ticked Analyses, add new record that matches Analyses to new .ana file
            Link new .ana file to active model

        Context:
            Form
            Get data for current model

        Returns:
            re-renders new_ana with updated data

    """
    BSM_instance = BSM_Model.objects.get(name=name)
    if request.method == 'POST':
        form = AnalysesForm(request.POST, request.FILES)
        ana_name = form['name'].value()
        author = form['author'].value()

        list_object,list_created = ana_list.objects.get_or_create(ana_name=ana_name,author=author)

        for analyses in form['analyses']:
            if 'checked' in analyses.tag():
                analyses = analyses.choice_label
                ana_object = Analysis.objects.get(anaid=analyses)

                ana_object,ana_created = ana_file.objects.get_or_create(linked_ana=list_object,anaid=ana_object)

        used_analyses.objects.get_or_create(ana_name=list_object,modelname=BSM_instance)

    else:
        form = AnalysesForm()



    return render(request, 'analyses/new_ana.html', {
        'form': form,
        'm':BSM_instance
    })

def write_ana(request,name):
    """
        Purpose:
            Write .ana file from database and download

        Parameters:
            Web request -> Activated by clicking on download .ana link
            name -> name of .ana file

        Operations:
            Find all linked analyses to active .ana file
            Create temporary text file with analyses entered in correct format
            Create wrapper and present to user for download
            Delete temporary file

        Context:
            No Specific Context

        Returns:
            Refreshes current page

    """
    try:
        ana = ana_list.objects.filter(ana_name=name)
        data = ana_file.objects.filter(linked_ana=ana[0]).values_list('anaid')

        f = open("analyses/tmp/" + str(name) + ".ana","w+")
        for analyses in data:
            line = analyses[0]
            f.write("insert Rivet:Analyses 0 " + line + "\n")
        f.close()

        try:
            wrapper = FileWrapper(open("analyses/tmp/"  + str(name) + ".ana" , 'rb'))
            response = HttpResponse(wrapper, content_type='application/force-download')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename("analyses/tmp/" + str(name) + ".ana")
            os.remove("analyses/tmp/" + str(name) + ".ana")
            return response

        except Exception as e:
            return None

    except:
        raise Http404()

def render_histo(request,id):
    """
        Purpose:
         Render png image of histogram to interface

        Parameters:
         Web request -> Activated by clicking on histogram link
         id -> id of histogram

        Operations:
            Find image from ID and render

        Context:
            Image location in media

        Returns:
            Loads image in new page

    """
    image = histo_images.objects.filter(id=id)

    context = {
        'image':image[0]
    }
    return render(request, 'analyses/histo_image.html', context)

def create_file(request,name):
    """
            Purpose:
                Uploads file to system linked to results header

            Parameters:
                Web request -> Comes from 'Add new file' link.
                Has no data specific arguments

            Operations:
                Saves new file to database through form

            Context:
                No Specific Context

            Returns:
                Renders File Upload form

        """
    res_head = results_header.objects.get(name=name)

    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            file = form['file'].value()
            name = form['name'].value()
            attached_files.objects.create(file=file,name=name,parent=res_head)
    else:
        form = FilesForm()

    return render(request, 'analyses/file_upload.html', {
        'form': form
    })

def create_paper(request,name):
    """
            Purpose:
                Uploads paper to system linked to results header

            Parameters:
                Web request -> Comes from 'Add new file' link.
                Has no data specific arguments

            Operations:
                Saves new file to database through form

            Context:
                No Specific Context

            Returns:
                Renders File Upload form

        """
    res_head = results_header.objects.get(name=name)
    if request.method == 'POST':
        form = PaperForm(request.POST, request.FILES)
        if form.is_valid():
            file = form['file'].value()
            name = form['name'].value()
            attached_papers.objects.create(file=file, name=name, parent=res_head)
    else:
        form = PaperForm()

    return render(request, 'analyses/file_upload.html', {
        'form': form
    })

def download_att_file(request,name):
    file = attached_files.objects.get(name=name)
    file_path = os.getcwd() + "/media/" + str(file.file)

    if "pdf" in file_path:
        content = 'application/pdf'
    else:
        content = 'text/plain'

    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type=content)
        response['Content-Disposition'] = 'attachment; filename=' + str(file.file)
        return response
    raise Http404