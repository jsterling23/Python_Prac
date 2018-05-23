from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.process_login_data, name='try_login'),
    url(r'^logout/$', views.log_out, name='log_out'),
]
