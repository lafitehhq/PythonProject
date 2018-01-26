from django.conf.urls import patterns, include, url
from django.contrib import admin
from web_manage.views import home

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sparta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index.html$', home.index),
    url(r'^about.html$', home.about),
    url(r'^teacher.html$', home.teacher),
    url(r'^students.html$', home.students),
    url(r'^problems.html$', home.problems),
    url(r'^videos'
        r'-(?P<direction_id>\d*)'
        r'-(?P<classification__id>\d*)'
        r'-(?P<level>\d*).html$', home.videos),
    url(r'', home.index),
)
