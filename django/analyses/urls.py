from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    # Index URL loads dashboard homepage
    url(r'^$', views.index, name='index'),

    # analysis URL loads information for a particular analysis
    url(r'^(?P<anaid>[_A-Za-z0-9]+)/$', views.analysis, name='analysis'),

    # model URL loads information for a particular model
    url(r'^model/(?P<name>[_A-Za-z0-9]+)/$', views.model, name='model'),

    # blacklist URL loads information for a blacklist
    url(r'^(?P<anaid>[_A-Za-z0-9]+)/blacklists/$', views.blacklists, name='blacklists'),

    # pool URL loads information for a pool and associated analysis data
    url(r'^pool/(?P<pool>[_A-Za-z0-9]+)/$', views.pool, name='pools'),

    # Upload url allows upload of a new analysis
    url(r'^upload', views.model_form_upload, name='upload'),

    # export URL downloads a model
    url(r'^export', views.model_form_download, name='export'),

    # keyword URL provides all data for a keyword
    url(r'^keyword/(?P<key_word>[_A-Za-z0-9]+)/$', views.keywords_list, name='keyword'),

    # Runcard URL loads the relevent section of the app for presenting and adding runcard data
    url(r'^runcard/(?P<runcard_name>[_A-Za-z0-9]+)/$', views.Runcard, name='runcard'),

    # Results URL leads to results header page, which contains all results information
    url(r'^results/(?P<name>[_A-Za-z0-9]+)/$', views.results, name='results'),

    # Fetch keywords URL collects keywords data from inspire
    url(r'^fetch_keywords', views.upload_keywords, name='load_kws'),

    # Produce Heatmap URL collects runs generate heatmap script for active data and generates interactive heatmap using Bokeh
    url(r'^produce_heatmap/(?P<analyses>[_A-Za-z0-9]+)/$',views.heatmap_display, name='produce_heatmap'),

    # Positions URL loads second layer of YODA data, specifically around the data for each combination of parameters
    url(r'^positions/(?P<id>[_A-Za-z0-9]+)/$',views.positions, name='positions'),

    # ana_data URL loads all information for a .ana file
    url(r'^ana_data/(?P<id>[_A-Za-z0-9]+)/$',views.ana_data, name='ana_data'),

    # ufo_home URL loads ufo form to add new model using UFO link
    url(r'^ufo_home', views.ufo_home, name='ufo_home'),

    # Download HTML URL allows histogram HTML data to be downloaded in a zip file
    url(r'^download_html/(?P<id>[_A-Za-z0-9]+)/$', views.download_html, name='html_render'),

    # dl_bsm URL downloads a BSM model stored in local files
    url(r'^dl_bsm/(?P<name>[_A-Za-z0-9]+)/$', views.dl_bsm, name='dl_bsm'),

    # add_ana URL renders page to display user with different options for associating new .ana file to a model
    url(r'^add_ana/(?P<name>[_A-Za-z0-9]+)/$', views.add_ana, name='add_ana'),

    # [ana_file URL is to be removed]
    url(r'^ana_file/(?P<name>[_A-Za-z0-9]+)/$', views.ana_file_view, name='ana_file'),

    # add_existing_ana URL associates an existing .ana file with active model
    url(r'^add_existing_ana/(?P<modelname>[_A-Za-z0-9]+)/(?P<name>[_A-Za-z0-9]+)/$', views.add_existing_ana, name='add_existing_ana'),

    # inside_ana URL renders information about active .ana file
    url(r'^inside_ana/(?P<ana_name>[_A-Za-z0-9]+)/$', views.inside_ana, name='inside_ana'),

    # new_ana URL allows user to create new_ana file
    url(r'^new_ana/(?P<name>[_A-Za-z0-9]+)/$', views.new_ana, name='new_ana'),

    # write_ana URL exports .ana file in correct format
    url(r'^write_ana/(?P<name>[_A-Za-z0-9]+)/$', views.write_ana, name='write_ana'),

    # Pool input URL loads form to create a new analysis pool
    url(r'^pool_input', views.pool_form, name='pool_input'),

    # Render histo URL to render histogram image when link is clicked on results page
    url(r'^render_histo/(?P<id>[_A-Za-z0-9]+)/$', views.render_histo,name='render_histo')

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
