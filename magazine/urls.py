from django.conf.urls import url
from magazine import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]