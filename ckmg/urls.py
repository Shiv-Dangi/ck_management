from django.conf.urls import patterns, url
from django.conf import settings
from ckmg import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^ckmg/header/$', views.header_info, name='header_info'),
    url(r'^ckmg/footer/$', views.footer_info, name='footer_info'),
    url(r'^ckmg/aboutus/$', views.aboutus_info, name='aboutus_info'),
    url(r'^ckmg/theorynotes/$', views.theorynotes_info, name='theorynotes_info'),
    url(r'^ckmg/modelpapers/$', views.modelpapers_info, name='modelpapers_info'),
    url(r'^ckmg/ppt/$', views.ppt_info, name='ppt_info'),
    url(r'^ckmg/project/$', views.project_info, name='project_info'),
    url(r'^ckmg/businessplan/$', views.businessplan_info, name='businessplan_info'),
    url(r'^ckmg/service/$', views.service_info, name='service_info'),
    url(r'^ckmg/training/$', views.training_info, name='training_info'),
    url(r'^ckmg/guidance/$', views.guidance_info, name='guidance_info'),
    url(r'^ckmg/contact/$', views.contact_info, name='contact_info'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)
