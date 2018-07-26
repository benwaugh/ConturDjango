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


]
