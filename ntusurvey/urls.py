from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import TemplateView
#from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),


    #url(r'^showIP/$', 'survey.cxq_views.showIP'),
    #url(r'^result/$', 'survey.cxq_views.result'),
    url(r'^add_component/$', 'survey.cxq_views.add_component'),
    url(r'^add_component/(?P<surveyID>\d+)/$', 'survey.cxq_views.add_component'),
    url(r'^delete_survey_cxq/$','survey.cxq_views.delete_survey'),
    # url(r'^cxqtestmutiajax/$','survey.cxq_views.multiajax'),

    url(r'^(\d+)/cxq_save_survey/$','survey.cxq_views.save_survey'),
    url(r'^create_survey_cxq/$','survey.cxq_views.create_survey'),
    url(r'^create_response/$','survey.views.create_response'),
    url(r'^view_survey/(?P<view_key>\w+)/$', 'survey.views.view_survey'),
    url(r'^response/(?P<responseID>\w+)/$', 'survey.views.response_survey'),
    url(r'^print_survey/(?P<view_key>\w+)/$', 'survey.views.print_survey'),

    url(r'^account/register/$',  'survey.account_views.register'),
    url(r'^account/confirm/(.*)/(.*)',  'survey.account_views.confirm'),
    url(r'^account/login/$',  'survey.account_views.login_view'),
    url(r'^account/signup/$', 'survey.views.signup'),
    url(r'^account/check_username/$', 'survey.account_views.check_username'),
    url(r'^account/check_email/$', 'survey.account_views.check_email'),
    url(r'^account/password_reset/$', 'django.contrib.auth.views.password_reset'),
    url(r'^account/edit_profile/',  'survey.account_views.edit_profile'),
    url(r'^account/logout/$', 'survey.account_views.logout_view'),
    url(r'^account/change_password/$', 'survey.account_views.change_password_view'),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^test/$', 'survey.views.test_view'),
    url(r'^$', 'survey.views.home'),
    url(r'^account/$', 'survey.views.account'),
    url(r'^edit_survey/$', 'survey.views.edit_survey'),
    url(r'^edit_survey/(\w+)/$', 'survey.views.edit_survey'),
    url(r'^analyse/(\w+)/$', 'survey.views.analyse'),
    url(r'^(\d+)/save_survey/$','survey.views.save_survey'),
    url(r'^create_survey/$','survey.views.create_survey'),
    url(r'^delete_survey/(?P<survey_key>\w+)/$','survey.views.delete_survey'),
    url(r'^delete_survey/$','survey.views.delete_survey'),

    url(r'^account/analyse/$', 'survey.views.analyse'),

    url(r'^respondent/$', 'survey.views.respondent'),
    url(r'^about/$', 'survey.views.about'),
    url(r'^account/display_users_function/$', 'survey.account_views.get_users_list'),
    url(r'^account/display_users/$', 'survey.account_views.get_users_list_index'),
    url(r'^publish/(\w+)/$','survey.views.publish'),
    url(r'^error_jump/(\w+)/$',"survey.views.error_jump"),
    url(r'^validate_answer/$',"survey.views.validate_answer"),
    url(r'^validate_survey/$',"survey.views.validate_survey"),
    url(r'^complete/(\w+)/$', 'survey.views.complete'),

    url(r'^collaborate/invite/$',  'survey.collaborate_views.invite'),
    url(r'^collaborate/accept/(.*)',  'survey.collaborate_views.accept'),
    url(r'^collaborate/delete/(.*)$','survey.collaborate_views.delete'),
    url(r'^collaborate/remove_collaborator/(.*)/(.*)$','survey.collaborate_views.remove_collaborator'),
    url(r'^share_survey/$','survey.views.share_survey'),

    url(r'/$',"survey.views.error_jump",{'error_type':'404'}),

)
urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

)

handler404 = 'survey.views.error_jump'
