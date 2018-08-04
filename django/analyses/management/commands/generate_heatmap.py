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
from bokeh.models import HoverTool

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(CURRENT_DIR)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(CURRENT_DIR))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contur_db.settings")
django.setup()

from analyses.models import runcard, results_header,map_header,map_pickle

pgf_with_rc_fonts = {"pgf.texsystem": "pdflatex"}
matplotlib.rcParams.update(pgf_with_rc_fonts)

# function to decode the physical X value from the x axis grid variable
def xlab(x, dummy=0):
#    if opts.SCAN == "ZPGP":
#        return np.power(10, x / 10.0)
#    else:
        return x


# function to decode the physical Y value from the y axis variable
def ylab(y, dummy=0):
#    if opts.SCAN == "MH2SA":
#        y = np.sin(y * np.pi / 40.0)
#        return float('%4.2f' % y)
#    elif opts.SCAN == "ZPGP":
#        lab = 1.0 * np.power(10, -y / 4.0)
#        return lab
#    else:
        return y


# -------------------------- MAIN -----------------------
def gen_heatmap(temp):

    contourXaxis = []
    contourYaxis = []
    modeMessage = ""

    #climit = float(opts.CLIMIT)
    climit = float(0.95)

    # Axis labels (should get these from the conturDepot eventually?)
    #if opts.SCAN == "MH2SA":
    #    xAxisLabel = r"$M_{h_2}$ [GeV]"
    #    yAxisLabel = r"$\sin \alpha$"
    #elif opts.SCAN == "ZPGP":
    #    xAxisLabel = r"$M_{Z'}$ [GeV]"
    #    yAxisLabel = r"$g'$"
    #else:
    xAxisLabel = r"$M_{Z'}$ [GeV]"
    yAxisLabel = r"$M_{\textsc{dm}}$ [GeV]"

    # Place to hold a conturDepot for each parameter point
    depots = {}

    # Build a dictionary to store the CL values for all this individual analysis pools for each paramter point
    confLims = defaultdict(list)
    bestPlots = {}

    # array to store the total CL values this is maximum possible size (ie too big!)
    confLim = np.zeros((1000, 1000))

    x = temp[0]
    n_pools = len(x[0].sortedPoints)

    #print(("Loaded file", m, " which has ", n_pools, " pools"))

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

    print("Recalculating")

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
        print("Setting up plots")

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


        # translate from the parameters of the  to something more readable
        #fmt = plt.FuncFormatter(xlab)
        #fmt2 = plt.FuncFormatter(ylab)

        # make an html index file for browsing them

        #index = open("./plots/index.html", "w")
        #index.write('<html>\n<head>\n<title>Heatmaps and contours</title>\n</head>\n<body>')

        # make the overall heatmap
        print("Overall heatmap")

        #fig = plt.figure(figsize=fig_dims)

        #ax = fig.add_subplot(1, 1, 1)
        #ax.xaxis.set_major_formatter(fmt)
        #ax.yaxis.set_major_formatter(fmt2)

        #if (opts.SCAN == "ZPGP"):
        #    my_locator_x = MaxNLocator((int(max(Xaxis)) / 10) + 1)
        ##    my_locator_y = MaxNLocator((int(max(Yaxis)) / 4) + 1)
        #    ax.yaxis.set_major_locator(my_locator_y)
        #    ax.xaxis.set_major_locator(my_locator_x)

        #plt.pcolormesh(xx, yy, cl_values.T, cmap=plt.cm.magma, vmin=0, vmax=1)
        # axis labels
        #plt.xlabel(xAxisLabel)
        #plt.ylabel(yAxisLabel)

        #x_grid_min = min(Xaxis)
        #HeatMap_Limits = False
        #if HeatMap_Limits:

            #if opts.SCAN == "DMLF":
                # plot the pert unitarity bound
        #         xub = np.array(Xaxis)
        #         xub[0] = xub[0] - dx
        #         yub = util.pertUnit(xub)
        #         plt.ylim(min(Yaxis) - dy, max(Yaxis) + dy)
        #         plt.plot(xub, yub, color='navy')
        #         ax.fill_between(xub, yub, max(Yaxis) + dy, facecolor='navy', alpha=0.4)
        #     elif opts.SCAN == "ZPGP":
        #         plt.ylim(min(Yaxis) - dy, max(Yaxis) + dy)
        #         plt.xlim(min(Xaxis) - dx, max(Xaxis) + dx)
        #         # plot the LEP bound
        #         y = np.array(Yaxis)
        #         x = util.LEPLimit(ylab(y))
        #         plt.plot(x, y, color='navy')
        #         ax.fill_between(x, y, x_grid_min, facecolor='navy', alpha=0.3)
        #         # plot the ATLAS bound
        #         y = np.array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10])
        #         x = util.ATLASLimit(ylab(y))
        #         plt.plot(x, y, color='navy')
        #         ax.fill_between(x, y, x_grid_min, facecolor='navy', alpha=0.2)
        #         # plot the Borexino bound
        #         y = np.array(Yaxis)
        #         y[0] = y[0] - dy
        #         x = util.BorexinoLimit(ylab(y))
        #         plt.plot(x, y, color='navy')
        #         ax.fill_between(x, y, x_grid_min, facecolor='navy', alpha=0.3)
        #         # make g' go the right way.
        #         plt.gca().invert_yaxis()
        #
        # elif opts.SCAN == "ZPGP":
        #     # make g' go the right way.
        #     plt.gca().invert_yaxis()

        # save the fig and pad it for better layout
        #fig.tight_layout(pad=0.1)
        #pngfile = "./plots/combinedCL.png"
        #contourpng = "./plots/contur.png"
        #pdffile = "./plots/combinedCL.pdf"
        #plt.savefig(pdffile)
        #plt.savefig(pngfile)

        #index.write('<h3>Combined Heatmap and contour</h3>')
        #index.write('<h4>' + modeMessage + '</h4>')
        #index.write('<img src="%s">\n' % os.path.basename(pngfile))
        #index.write('<img src="%s">\n' % os.path.basename(contourpng))

        # now the heatmaps for the different analysis pools
        #print()
        #"Subpool heatmaps"
        #for pool in confLims:

            #cl_values_pool = confLims[pool][:len(contourXaxis), :len(contourYaxis)]

            #fig = plt.figure(figsize=fig_dims)
            #ax = fig.add_subplot(1, 1, 1)
            #ax.xaxis.set_major_formatter(fmt)
            #ax.yaxis.set_major_formatter(fmt2)
            #if opts.SCAN == "ZPGP":
            #    ax.yaxis.set_major_locator(my_locator_y)
            #    ax.xaxis.set_major_locator(my_locator_x)

            #plt.pcolormesh(xx, yy, cl_values_pool.T, cmap=plt.cm.magma, vmin=0, vmax=1)

            # axis labels
            #plt.xlabel(xAxisLabel)
            #plt.ylabel(yAxisLabel)

            # save the fig and pad it for better layout
            #if opts.SCAN == "ZPGP":
            #    plt.gca().invert_yaxis()
            #fig.tight_layout(pad=0.1)
            #pngfile = "./plots/combinedCL_" + pool + ".png"
            #plt.savefig(pngfile)
            #index.write('<h4>%s</h4>' % pool)
            #index.write('<img src="%s">\n' % os.path.basename(pngfile))
            #if pool in bestPlots:
            #    index.write(bestPlots[pool])

            #plt.close(fig)

        # Now the overall contour plot -------------------------------------------------------------------------------
        print("Overall contour plot")


        #fig = plt.figure(figsize=fig_dims)

        #ax = fig.add_subplot(1, 1, 1)
        #ax.xaxis.set_major_formatter(fmt)
        #ax.yaxis.set_major_formatter(fmt2)
        #if (opts.SCAN == "ZPGP"):
        #    ax.yaxis.set_major_locator(my_locator_y)
        #    ax.xaxis.set_major_locator(my_locator_x)

        # draw a filled contour region for the CL excl
        #plt.contourf(Xaxis, Yaxis, cl_values.T, levels=[climit, 1.0], label="CL", cmap=plt.cm.magma, alpha=0.8)
        # and a black outline
        #CS2 = plt.contour(CS, colors='black')

        # axis labels
        #plt.xlabel(xAxisLabel)
        #plt.ylabel(yAxisLabel)

        # if opts.SCAN == "DMLF":
        #     # plot the pert unitarity bound
        #     xub = np.array(Xaxis)
        #     yub = util.pertUnit(xub)
        #     plt.ylim(min(Yaxis) - dy, max(Yaxis))
        #     plt.plot(xub, yub, color='navy')
        #     ax.fill_between(xub, yub, max(Yaxis), facecolor='navy', alpha=0.4)
        # elif opts.SCAN == "ZPGP":
        #     plt.ylim(min(Yaxis), max(Yaxis))
        #     plt.xlim(min(Xaxis), max(Xaxis))
        #     # plot the LEP bound
        #     # y=np.array(Yaxis)
        #     # x=util.LEPLimit(ylab(y))
        #     # plt.plot(x,y,color='navy')
        #     # ax.fill_between(x,y,x_grid_min,facecolor='navy',alpha=0.3)
        #     # plot the ATLAS bound
        #     y = np.array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10])
        #     x = util.ATLASLimit(ylab(y))
        #     plt.plot(x, y, color='navy')
        #     ax.fill_between(x, y, x_grid_min, facecolor='navy', alpha=0.2)
        #     plt.text(31.0, 3., "ATLAS", color='navy', rotation="65")
        #     # plot the Borexino bound
        #     y = np.array(Yaxis)
        #     x = util.BorexinoLimit(ylab(y))
        #     plt.plot(x, y, color='orange')
        #     ax.fill_between(x, y, x_grid_min, facecolor='orange', alpha=0.2)
        #     plt.text(10.0, 4., "Borexino", color='orange', rotation="45")
        #
        #     # the theory constraints
        #     th_x = np.arange(min(Xaxis), max(Xaxis) + dx, 1.0)
        #     th_y = np.arange(min(Yaxis), max(Yaxis), 0.01)
        #     th_values = np.zeros((len(th_x), len(th_y)))
        #     for i, x in enumerate(th_x):
        #         for j, y in enumerate(th_y):
        #             # ------------------
        #             mzp = xlab(x).item()
        #             g1p = ylab(y).item()
        #             #               mh2 = mzp/(2.0*g1p)
        #             #               sina = 0.0
        #             mh2 = 200.
        #             sina = 0.4
        #             # ------------------
        #             #               sina = 4.0*1.772*g1p*246.0/mzp
        #             #               if sina > 0.4:
        #             #                   sina = 0.4
        #             # ------------------
        #             vacon, percon, vapercon = util.bl3theory(mzp, g1p, mh2, sina)
        #             th_values[i][j] = 1.0 - vapercon
        #
        #     # draw a filled contour region for the CL excl
        #     CS = plt.contourf(th_x, th_y, th_values.T, levels=[climit, 1.0], label="CL", cmap=plt.cm.Greys, alpha=0.4)
        #     # and a black outline
        #     CS2 = plt.contour(CS, colors='red')
        #
        #     # make g' go the right way.
        #     plt.gca().invert_yaxis()
        #
        # elif opts.SCAN == "MH2SA":
        #     # the theory constraints
        #     th_x = np.arange(min(Xaxis), max(Xaxis), 5.0)
        #     th_y = np.arange(min(Yaxis), max(Yaxis), 0.05)
        #     th_values = np.zeros((len(th_x), len(th_y)))
        #     for i, x in enumerate(th_x):
        #         for j, y in enumerate(th_y):
        #             mh2 = xlab(x).item()
        #             sina = ylab(y)
        #             mzp = 7000.
        #             g1p = 1.0
        #             vacon, percon, vapercon = util.bl3theory(mzp, g1p, mh2, sina)
        #             th_values[i][j] = 1.0 - vapercon
        #
        #     # draw a filled contour region for the CL excl
        #     CS1 = plt.contourf(th_x, th_y, th_values.T, levels=[climit, 1.0], label="CL", cmap=plt.cm.Greys, alpha=0.4)
        #     # and a black outline
        #     CS3 = plt.contour(CS1, colors='red')

        #fig.tight_layout(pad=0.1)
        #plt.savefig("./plots/contur.pdf")
        #plt.savefig("./plots/contur.png")



        # Now the colour bar key --------------------------------------------------------------------------

        #cbar = plt.figure(1, figsize=[fig_dims[0] * 2, 0.5])

        #ax = cbar.add_subplot(1, 1, 1)

        #import matplotlib as mpl

        #norm = mpl.colors.Normalize(vmin=0, vmax=1)
        #mpl.colorbar.ColorbarBase(ax, cmap=plt.cm.magma, orientation='horizontal', norm=norm)
        #cbar.set_label("CL of exclusion")
        #cbar.tight_layout(pad=0.1)
        #plt.savefig('./plots/colorbarkey.pdf')
        #plt.savefig('./plots/colorbarkey.png')

        # close the html file
        #index.write("\n </body> \n")
        #index.close()
    d = cl_values.T

    def max_value(inputlist):
        return max([sublist[-1] for sublist in inputlist])

    ca_list = [ [None] * np.shape(d)[1] ] * np.shape(d)[0]
    i = 0
    for x in contributing_analyses:
        j = 0
        for y in contributing_analyses[x]:
            ca_list[j][i] = (str(contributing_analyses[x][y]))
            j = j + 1
        i = i + 1


    hg_list = [[None] * np.shape(d)[1]] * np.shape(d)[0]
    i = 0
    for x in contributing_histos:
        j = 0
        for y in contributing_histos[x]:
            if j == 0 and i ==0:
                hg_list[j][i] = "S"
            else:
                hg_list[j][i] = (str(contributing_histos[x][y]))
            j = j + 1
        i = i + 1
    print(hg_list)

    hover = HoverTool(
        tooltips=[("x", "$x"), ("y", "$y"), ("value", "@image"),("Contributing Analyses","@ca_list"),("Contributing Histograms","@hg_list")]
    )

    data = ColumnDataSource(
        dict(
            image = [d],
            ca_list = [ca_list],
            hg_list = [hg_list]
             )
    )

    p = figure(x_range=(0, max_value(xx)), y_range=(0, max_value(yy)),
               tools=[hover,"crosshair","pan","box_zoom","wheel_zoom","reset","save"])

    # must give a vector of image data for image parameter
    p.image(source=data,image='image' , x=0, y=0, dw=max_value(xx), dh=max_value(yy), palette="Magma256")

    output_file("image.html", title="image.py example")
    show(p)
