from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^delete/$', views.delete_session, name='delete_session'),
    url(r'^random_string/$', views.random_string, name='random_string'),
]
