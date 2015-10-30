from django.conf.urls import patterns, url
from django.conf import settings
from ckmg import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^ckmg/header/$', views.header_info, name='header_info'),
    url(r'^ckmg/footer/$', views.footer_info, name='footer_info'),
    url(r'^ckmg/aboutus/$', views.aboutus_info, name='aboutus_info'),
    
    #Mind Program urls
    url(r'^ckmg/dmitanalysis/$', views.dmit_info, name='dmit_info'),
    url(r'^ckmg/urja/$', views.urja_info, name='urja_info'),
    url(r'^ckmg/success_club/$', views.success_club_info, name='success_club_info'),
    url(r'^ckmg/other_mind_programming/$', views.other_mind_programming_info, name='other_mind_programming_info'),

    # Library menu urls
    url(r'^ckmg/theorynotes/$', views.theorynotes_info, name='theorynotes_info'),
    url(r'^ckmg/theorynotes/(?P<pm>\w+)/$', views.theorynotes_subject, name='theorynotes_subject'),
    url(r'^ckmg/modelpapers/$', views.modelpapers_info, name='modelpapers_info'),
    url(r'^ckmg/modelpapers/(?P<pm>\w+)/$', views.modelpapers_subject, name='modelpapers_subject'),
    url(r'^ckmg/ppt/$', views.ppt_info, name='ppt_info'),
    url(r'^ckmg/ppt/(?P<pm>\w+)/$', views.ppt_subject, name='ppt_subject'),
    url(r'^ckmg/project/$', views.project_info, name='project_info'),
    url(r'^ckmg/businessplan/$', views.businessplan_info, name='businessplan_info'),

    #services menu urls
    url(r'^ckmg/service/$', views.service_info, name='service_info'),
    url(r'^ckmg/training/$', views.training_info, name='training_info'),
    url(r'^ckmg/guidance/$', views.guidance_info, name='guidance_info'),
    url(r'^ckmg/contact/$', views.contact_info, name='contact_info'),

    # user auth urls
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/auth/$', views.auth_view, name='auth_view'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
    url(r'^accounts/invalid/$', views.invalid_login, name='invalid_login'),
    url(r'^accounts/register/$', views.register_user, name='register_user'),
    url(r'^accounts/register_success/$', views.register_success, name='register_success'),
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)
