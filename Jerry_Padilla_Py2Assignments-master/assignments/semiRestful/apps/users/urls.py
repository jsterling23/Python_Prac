from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^process_add/$', views.process_add, name='process_add'),
    url(r'^show/(?P<user_id>\d+)/$', views.show, name='show'),
    url(r'^edit/(?P<user_id>\d+)/$', views.edit, name='edit'),
    url(r'^process_edit/(?P<user_id>\d+)/$', views.process_edit, name='process_edit'),
    url(r'^destory/(?P<user_id>\d+)/$', views.destroy, name='destroy'),
]
