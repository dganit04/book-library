from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'libapp.views.index', name='index'),
    url(r'^item/(?P<id>\d+)/', 'libapp.views.item_detail', name='item_detail'),
    url(r'^delete/(?P<id>\d+)/', 'libapp.views.item_delete', name='item_delete'),
    # url(r'^form/', 'libapp.views.item_form', name='item_form'),
    # url(r'^update/(?P<id>\d+)/', 'libapp.views.item_update', name='item_update'),
    url(r'^update-create/(?P<id>\d+)/', 'libapp.views.item_create_update', name='item_create_update'), # update with id
    url(r'^update-create/(?P<id>\w+)/', 'libapp.views.item_create_update', name='item_create_update'), # create new with id='a'
    url(r'^reset/', 'libapp.views.reset', name='reset'),
    url(r'^admin/', include(admin.site.urls)),
)
