from django.conf.urls.defaults import *
from book.views import search

urlpatterns = patterns('',
    url(r'^$',search),
)