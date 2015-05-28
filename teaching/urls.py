from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('',
                       url(r'^subjects/$', views.subjects, name='subjects'),
                       url(r'^subject/(?P<subject_id>\d+)$', views.subject, name='subject'),
                       url(r'^paragraph/(?P<paragraph_id>\d+)$', views.paragraph, name='paragraph'),
                       url(r'^chapter/(?P<chapter_id>\d+)$', views.chapter, name='chapter'),
                       )