from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process_form_data/$', views.process_form_data, name='process_form_data'),
    url(r'^delete_session', views.delete_session, name='delete_session'),
]
