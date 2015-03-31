'''
Created on Feb 18, 2015

@author: jay7958
'''
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^engagement/(?P<eid>\d+)/add_survey$',
        'defectDojo_engagement_survey.views.add_survey',
        name='add_survey'),
    url(r'^engagement/(?P<eid>\d+)/survey/(?P<sid>\d+)/answer',
        'defectDojo_engagement_survey.views.answer_survey',
        name='answer_survey'),
    url(r'^engagement/(?P<eid>\d+)/survey/(?P<sid>\d+)/delete',
        'defectDojo_engagement_survey.views.delete_survey',
        name='delete_survey'),
    url(r'^engagement/(?P<eid>\d+)/survey/(?P<sid>\d+)$',
        'defectDojo_engagement_survey.views.view_survey',
        name='view_survey'),
)