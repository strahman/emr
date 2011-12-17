from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^$', redirect_to, ({'url': '/cards/'})),
    url(r'^cards/', include(admin.site.urls)),
)

# 
# if settings.DEBUG:
#     urlpatterns += patterns('',
#         (r'^static/(?P<path>.*)$', 'django.views.static.serve',
#             {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
# )
