from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process_data/$', views.process_data, name='process_data'),
    url(r'^clear_session/$', views.clear_session, name='clear_session'),
]
