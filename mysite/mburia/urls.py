from django.conf.urls import url, include

from . import views

app_name = 'mburia'
urlpatterns = [
	url(r'^$', views.index, name='mburia_home'),
	url(r'^ask/$', views.ask_question, name='ask_question'),
	url(r'^submit-question', views.submit_question, name='submit_query'),
	url(r'^category-questions/(?P<pk>\d+)/$', views.category_questions, name='category_questions'),
	url(r'^question-detail/(?P<pk>\d+)/$', views.question_detail, name='question_detail'),
	url(r'^submit-response/(?P<pk>\d+)/$', views.submit_answer, name='submit_answer'),
	url(r'^up-vote/(?P<pk>\d+)/(?P<question>\d+)/$', views.up_answer_vote, name='up_vote'),
	url(r'^down-vote/(?P<pk>\d+)/(?P<question>\d+)/$', views.down_answer_vote, name='down_vote'),
]