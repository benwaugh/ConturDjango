from optparse import OptionParser
import os, sys
import contur.Utils as util
import contur as ct
from contur.Plotting import *
import pickle
import os, sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.stats as sp
import scipy.ndimage
from os.path import join
import errno
from matplotlib.ticker import *
from collections import defaultdict
import django
import json
import mpld3
from bokeh.plotting import figure, show, output_file, ColumnDataSource
from bokeh.models import HoverTool,OpenURL, TapTool
from bokeh.layouts import gridplot
from django.core.exceptions import ObjectDoesNotExist
from bokeh.models.widgets import Dropdown
from bokeh.layouts import widgetbox
from bokeh.models.annotations import Title
from bokeh.layouts import column
from bokeh.io import export_png

# Load application
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(CURRENT_DIR)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(CURRENT_DIR))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contur_db.settings")
django.setup()

# Import models
from analyses.models import runcard, results_header,map_header,map_pickle, histo_images, results_position, histo_header

# Set backend matplotlib backing details
pgf_with_rc_fonts = {"pgf.texsystem": "pdflatex"}
matplotlib.rcParams.update(pgf_with_rc_fonts)


# From this point, code is the code from the 'contur' script unless explicitly mentioned:


# function to decode the physical X value from the x axis grid variable
def xlab(x, dummy=0):
        return x


# function to decode the physical Y value from the y axis variable
def ylab(y, dummy=0):
        return y


# -------------------------- MAIN -----------------------
def gen_heatmap(temp,header):


    # Function uses database data when called in order to plot

    contourXaxis = []
    contourYaxis = []
    modeMessage = ""

    #climit = float(opts.CLIMIT)
    climit = float(0.95)

    # Place to hold a conturDepot for each parameter point
    depots = {}

    # Build a dictionary to store the CL values for all this individual analysis pools for each paramter point
    confLims = defaultdict(list)
    bestPlots = {}

    # array to store the total CL values this is maximum possible size (ie too big!)
    confLim = np.zeros((1000, 1000))

    x = temp[0]
    n_pools = len(x[0].sortedPoints)

    # Sort them so the parameter values are in order.
    x.sort(key=lambda i: (float(i.ModelParam1), float(i.ModelParam2)))

    for ctp in x[0].sortedPoints:
        pool = ctp.pools
        confLims[pool] = np.zeros((len(x), len(x)))

    for cDepot in x:
        if not cDepot.ModelParam1 in contourXaxis:
            contourXaxis.append(cDepot.ModelParam1)
        if not cDepot.ModelParam2 in contourYaxis:
            contourYaxis.append(cDepot.ModelParam2)

        key = str(cDepot.ModelParam1) + "-" + str(cDepot.ModelParam2)
        if not key in depots:
            depots[key] = cDepot
        else:
            for ctpt in cDepot.sortedPoints:
                depots[key].sortedPoints.append(ctpt)



                # ended loop over points -------------------------------


                # ended loop over files -------------------------------


    contributing_analyses = dict()
    contributing_histos = dict()
    for key in depots:

        cDepot = depots[key]

        cDepot.buildFinal()

        confLim[contourXaxis.index(cDepot.ModelParam1)][contourYaxis.index(cDepot.ModelParam2)] = cDepot.conturPoint.CLs

        for ctp in depots[key].sortedPoints:



            confLims[ctp.pools][contourXaxis.index(cDepot.ModelParam1)][
                contourYaxis.index(cDepot.ModelParam2)] = ctp.CLs
            a = str(ctp.tags)

            if contourXaxis.index(cDepot.ModelParam1) not in contributing_analyses:
                contributing_analyses[contourXaxis.index(cDepot.ModelParam1)] = dict()
                contributing_analyses[contourXaxis.index(cDepot.ModelParam1)][
                    contourYaxis.index(cDepot.ModelParam2)] = []

            if contourXaxis.index(cDepot.ModelParam1) not in contributing_histos:
                contributing_histos[contourXaxis.index(cDepot.ModelParam1)] = dict()
                contributing_histos[contourXaxis.index(cDepot.ModelParam1)][
                    contourYaxis.index(cDepot.ModelParam2)] = []


            if contourYaxis.index(cDepot.ModelParam2) not in contributing_analyses[contourXaxis.index(cDepot.ModelParam1)]:
                contributing_analyses[contourXaxis.index(cDepot.ModelParam1)][
                    contourYaxis.index(cDepot.ModelParam2)] = []

            if contourYaxis.index(cDepot.ModelParam2) not in contributing_histos[contourXaxis.index(cDepot.ModelParam1)]:
                contributing_histos[contourXaxis.index(cDepot.ModelParam1)][
                    contourYaxis.index(cDepot.ModelParam2)] = []




            for item in a.split(',/'):
                ana = item.split('/')[0]

                if ana not in contributing_analyses[contourXaxis.index(cDepot.ModelParam1)][contourYaxis.index(cDepot.ModelParam2)] \
                        and ana is not '':
                    contributing_analyses[contourXaxis.index(cDepot.ModelParam1)][contourYaxis.index(cDepot.ModelParam2)].append(ana)

            for item in a.split(',/'):
                    contributing_histos[contourXaxis.index(cDepot.ModelParam1)][contourYaxis.index(cDepot.ModelParam2)].append(item)


            if ctp.CLs > 0.5 and not ctp.pools in bestPlots:
                bestPlots[ctp.pools] = ctp.tags + ":" + str(ctp.CLs)
                if ctp.CLs > 0.5 and not ctp.tags in bestPlots[ctp.pools]:
                    bestPlots[ctp.pools] = ctp.tags + ":" + str(ctp.CLs)

                        # set up for the plots here.

        Xaxis = np.array(list(map(float, contourXaxis)))
        Yaxis = np.array(list(map(float, contourYaxis)))

        # sort, just in case
        Xaxis.sort()
        Yaxis.sort()

        # find the grid spacings:

        dx = (min([x for x in (Xaxis) if x > min(Xaxis)]) - min(Xaxis)) / 2.0
        dy = (min([x for x in (Yaxis) if x > min(Yaxis)]) - min(Yaxis)) / 2.0
        # print dx, dy

        yy, xx = np.mgrid[min(Yaxis) - dy:max(Yaxis) + 2 * dy:2 * dy, min(Xaxis) - dx:max(Xaxis) + 2 * dx:2 * dx]

        cl_values = confLim[:len(contourXaxis), :len(contourYaxis)]


    d = cl_values.T
    cls = d.flatten()

    def max_value(inputlist):
        return max([sublist[-1] for sublist in inputlist])

    # ----------------- ALL BELOW CODE HAS BEEN ADDED AS PART OF CORD --------------------

    # Added Code: Create list of analyses that contribute to plot
    ca_list = [ [None] * np.shape(d)[1] ] * np.shape(d)[0]
    i = 0
    for x in contributing_analyses:
        j = 0
        for y in contributing_analyses[x]:
            ca_list[j][i] = (str(contributing_analyses[x][y]))
            j = j + 1
        i = i + 1

    # Added Code: Create list of histograms that contribute to plot
    hg_list = [[None] * np.shape(d)[1]] * np.shape(d)[0]
    histo_table = []
    parameter_table = []
    analyses_table = []

    i = 0
    for x in contributing_histos:
        j = 0

        for y in contributing_histos[x]:
            hg_list[j][i] = (str(contributing_histos[x][y]))
            z = 0
            temp_list = []
            name_list = []
            for histo in contributing_histos[x][y]:

                name = "mY_" + str(contourYaxis[y]) + "_mX_" + contourXaxis[x]
                try:
                    position = results_position.objects.get(name=name, parent=header)

                    histo_head = histo_header.objects.get(results_object=position.id)

                    item = histo.replace("[", "")
                    item = item.replace("'", "")
                    item = item.replace("]", "")

                    item = item.replace("/", " ")

                    item = item.lstrip()
                    item = item.replace(" ", "_")


                    name2 = str(item) + ".png"
                    name_list.append(str(item))
                    image = histo_images.objects.get(parent=histo_head,position=name2)
                    data = image.image
                    temp_list.append(data)

                except(ObjectDoesNotExist):
                    name_list.append("")
                    temp_list.append("not-found.png")
                    z = z + 1

            histo_table.append(temp_list)
            parameter_table.append(name)
            analyses_table.append(name_list)

            j = j + 1
        i = i + 1

    return histo_table,parameter_table,cls,analyses_table
