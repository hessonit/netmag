from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'netmag.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', "blog.views.main"),
    #url(r'^$', 'blog.views.index'),
    url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),
    url(r"^(\d+)/$", "blog.views.post"),
    url(r'^(?P<slug>[\w\-]+)/add_comment/$', 'blog.views.add_comment'),
)
