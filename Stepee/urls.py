from django.conf.urls import patterns, include, url
from django.contrib import admin

import others.urls
import teaching.urls
import customuser.urls
import exercises.urls

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       ) + others.urls.urlpatterns + teaching.urls.urlpatterns + customuser.urls.urlpatterns + exercises.urls.urlpatterns