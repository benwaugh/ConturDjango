from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<anaid>[_A-Za-z0-9]+)/$', views.analysis, name='analysis'),
    url(r'^model/(?P<name>[_A-Za-z0-9]+)/$', views.model, name='model'),
    url(r'^(?P<anaid>[_A-Za-z0-9]+)/blacklists/$', views.blacklists, name='blacklists'),
    url(r'^pool/(?P<pool>[_A-Za-z0-9]+)/$', views.pool, name='pools'),
]
