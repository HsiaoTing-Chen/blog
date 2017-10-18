"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib.auth.views import login, logout
from . import views

app_name = "blog"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^article/add/$', views.article_add, name='article_add'),
    url(r'^article/edit/(?P<article_id>[0-9]+)$', views.article_edit, name='article_edit'),
    url(r'^article/edit_save/(?P<article_id>[0-9]+)$', views.article_edit_save, name='article_edit_save'),
    url(r'^article/delete/(?P<article_id>[0-9]+)$', views.article_delete, name='article_delete'),
    url(r'^article/save/$', views.article_save, name='article_save'),
    url(r'^message/add/$', views.message_add, name='message_add'),
    url(r'^message/save/(?P<article_id>[0-9]+)$', views.message_save, name='message_save'),
    #url(r'^login/$', login, {'template_name': 'blog/login.html'}, name='login'),
    #url(r'^logout/$', logout, {'next_page': 'blog:logout'}),
]

