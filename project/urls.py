from cms.sitemaps import CMSSitemap
from django.conf.urls import *  # NOQA
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'cmspages': CMSSitemap}}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^', include('cms.urls')),
                            )


# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = i18n_patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ) + staticfiles_urlpatterns() + urlpatterns  # NOQA
