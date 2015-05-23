from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^subjects/$', views.subjects, name='subjects'),
    url(r'^subject/$', views.subject, name='subject'),
    url(r'^chapter/$', views.chapter, name='chapter'),
    url(r'^paragraph/$', views.paragraph, name='paragraph'),
)