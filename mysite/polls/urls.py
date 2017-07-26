from django.conf.urls import url

from . import views


app_name = 'polls'

urlpatterns = [
	url(r'^$', views.index, name='polls_home'),
	url(r'^question/(?P<pk>\d+)/$', views.question_detail, name='question_detail'),
	url(r'^question/(?P<pk>\d+)/vote/$', views.new_vote, name='new_vote'),
]