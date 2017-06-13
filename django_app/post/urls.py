from django.conf.urls import url
from . import views

# app_name = 'post'
# use post:name
urlpatterns = [
    url(r'^$', views.post_list, name="post_list"),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^create/$', views.post_create, name='post_create'),
    url(r'^(?P<pk>\d+)/modify/$', views.post_modify, name='post_modify'),

]
