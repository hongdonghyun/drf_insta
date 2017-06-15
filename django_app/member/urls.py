from django.conf.urls import url

from . import views
app_name ='member'

urlpatterns = [
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^signup/$',views.signup,name='sign'),
    url(r'^login/change_password/$',views.change_password,name='change_password')

]