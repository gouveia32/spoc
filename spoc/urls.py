# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin

from spoc import views

admin.autodiscover()

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers
from rest_framework.views import APIView

# ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     model = User

# class GroupViewSet(viewsets.ModelViewSet):
#     model = Group


router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)
#router.register(r'groups', GroupViewSet)
#router.register(r'locations', views.ListLocations)
#router.register(r'location', views.LocationDetails)
urlpatterns = patterns(
    'spoc.views',
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^locations/$', 'location_list'),
    #url(r'^locations/(?P<pk>[0-9]+)/$', 'location_detail'),
    url(r'^$', 'api_root'),
    #url(r'^locations/$', 'oei_list', name='oei-list'),
    url(r'^locations/$', 'location_header_list', name='location-header-list'),
    #url(r'^locations/(?P<pk>[0-9]+)/$', 'oei_detail', name='oei-detail'),
    url(r'^locations/(?P<pk>[0-9]+)/$', 'location_header_detail', name='locationheader-detail'),
    url(r'^headers/(?P<pk>[0-9]+)/$', 'header_detail', name='header-detail'),
    url(r'^oeilocations/(?P<pk>[a-zA-Z0-9_.-]+)/$', 'location_detail', name='location-detail'),

    url(r'^parameters/$', 'wnsattribute_list', name='wnsattribute-list'),
    url(r'^parameters/(?P<pk>[0-9]+)/$', 'wnsattribute_detail', name='wnsattribute-detail')
    
    
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^something/',
    #     views.some_method,
    #     name="name_it"),
    # url(r'^something_else/$',
    #     views.SomeClassBasedView.as_view(),
    #     name='name_it_too'),
    )
