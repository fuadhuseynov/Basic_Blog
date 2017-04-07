from django.conf.urls import url
from . import views

app_name = "posts"

urlpatterns = [
    #/posts/
    url(r'^$', views.post_list, name='post_list'),

    #/posts/<post_id>/
    url(r'^(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),

    #/posts/create/
    url(r'^create/$', views.post_create, name='post_create'),

    #/posts/<post_id>/edit/
    url(r'^(?P<post_id>\d+)/edit/$', views.post_update, name='post_update'),

    url(r'^(?P<post_id>\d+)/delete/$', views.post_delete, name='post_delete'),
]