from django.conf.urls import patterns, url


urlpatterns = patterns('dynamics.views',
    url(r'^new/$', 'new_dynamic', name='new_dynamic'),
    url(r'^attach-molecules/$', 'attach_molecules',
        name='attach_molecules'),
)