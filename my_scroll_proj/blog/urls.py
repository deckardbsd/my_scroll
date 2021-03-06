"""blog app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
        url(r'^$', views.IndexView.as_view(), name='post_list'),
        # if you want to use pk to link the model in template
        # url(r'^(?P<pk>[-\w]+)/$', views.DetailView.as_view(), name='post_detail')
        url(r'^(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), name='post_detail'),
        url(r'^delete/(?P<slug>[-\w]+)/$', views.PostDeleteView.as_view(), name='post_delete'),
        url(r'^update/(?P<slug>[-\w]+)/$', views.PostUpdateView.as_view(), name='post_update'),
        # url(r'^(?P<slug>[-\w]+)/$', views.PostView.as_view(), name='post_detail')
]

