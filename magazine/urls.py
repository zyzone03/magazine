from django.conf.urls import url, include
from magazine import views
from django.conf import settings
from django.conf.urls.static import static

extra_patterns = [
	url(r'^$', views.article_list, name="article_list"),
	url(r'^(?P<pk>\d+)/$', views.article_detail, name='article_detail'),
	url(r'^new/$', views.article_new, name="article_new"),
	url(r'^edit/(?P<pk>\d+)/$', views.article_edit, name="article_edit"),
	url(r'^delete/(?P<pk>\d+)/$', views.article_delete, name="article_delete"),
]


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^articles/', include(extra_patterns)),
	url(r'^articles/(?P<post_pk>\d+)/comment/new/$', views.comment_new, name='comment_new'),
    url(r'^articles/(?P<post_pk>\d+)/comment/(?P<pk>\d+)/edit$', views.comment_edit, name='comment_edit'),
    url(r'^articles/(?P<post_pk>\d+)/comment/(?P<pk>\d+)/delete$', views.comment_delete, name='comment_delete'),
]

urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
