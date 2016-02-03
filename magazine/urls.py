from django.conf.urls import url
from magazine import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^articles/$', views.article_list, name='article_list'),
	url(r'^articles/(?P<pk>\d+)/$', views.article_detail, name='article_detail'),

	url(r'^articles/new/$', views.article_new, name="article_new")

]