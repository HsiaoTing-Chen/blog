from django.conf.urls import url
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
]
