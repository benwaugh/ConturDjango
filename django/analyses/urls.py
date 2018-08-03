from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<anaid>[_A-Za-z0-9]+)/$', views.analysis, name='analysis'),
    url(r'^model/(?P<name>[_A-Za-z0-9]+)/$', views.model, name='model'),
    url(r'^(?P<anaid>[_A-Za-z0-9]+)/blacklists/$', views.blacklists, name='blacklists'),
    url(r'^pool/(?P<pool>[_A-Za-z0-9]+)/$', views.pool, name='pools'),
    url(r'^upload', views.model_form_upload, name='upload'),
    url(r'^export', views.model_form_download, name='export'),
    url(r'^keyword/(?P<key_word>[_A-Za-z0-9]+)/$', views.keywords_list, name='keyword'),
    url(r'^runcard/(?P<runcard_name>[_A-Za-z0-9]+)/$', views.Runcard, name='runcard'),
    url(r'^results/(?P<name>[_A-Za-z0-9]+)/$', views.results, name='results'),
    url(r'^fetch_keywords', views.upload_keywords, name='load_kws'),
    url(r'^produce_heatmap/(?P<analyses>[_A-Za-z0-9]+)/$',views.heatmap_display, name='produce_heatmap'),
    url(r'^positions/(?P<id>[_A-Za-z0-9]+)/$',views.positions, name='positions'),
    url(r'^ana_data/(?P<id>[_A-Za-z0-9]+)/$',views.ana_data, name='ana_data'),
    url(r'^ufo_home', views.ufo_home, name='ufo_home'),
    url(r'^download_html/(?P<id>[_A-Za-z0-9]+)/$', views.download_html, name='html_render'),
    url(r'^dl_bsm/(?P<name>[_A-Za-z0-9]+)/$', views.dl_bsm, name='dl_bsm'),
    url(r'^add_ana/(?P<name>[_A-Za-z0-9]+)/$', views.add_ana, name='add_ana'),
    url(r'^ana_file/(?P<name>[_A-Za-z0-9]+)/$', views.ana_file_view, name='ana_file'),
    url(r'^add_existing_ana/(?P<modelname>[_A-Za-z0-9]+)/(?P<name>[_A-Za-z0-9]+)/$', views.add_existing_ana, name='add_existing_ana'),
    url(r'^inside_ana/(?P<ana_name>[_A-Za-z0-9]+)/$', views.inside_ana, name='inside_ana'),
    url(r'^new_ana/(?P<name>[_A-Za-z0-9]+)/$', views.new_ana, name='new_ana'),
    url(r'^write_ana/(?P<name>[_A-Za-z0-9]+)/$', views.write_ana, name='write_ana'),
    url(r'^pool_input', views.pool_form, name='pool_input'),
]
