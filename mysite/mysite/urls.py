from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^search/$','book.views.search' ),
    url(r'^save_book/$','book.views.save_book' ),
    url(r'^save_author/$','book.views.save_author' ),
    url(r'^look/', 'book.views.look'),
    url(r'^updata/', 'book.views.updata'),
    url(r'^delete/', 'book.views.delete'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
