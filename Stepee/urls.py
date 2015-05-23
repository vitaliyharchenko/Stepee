from django.conf.urls import patterns, include, url
from django.contrib import admin

import others.urls

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
) + others.urls.urlpatterns