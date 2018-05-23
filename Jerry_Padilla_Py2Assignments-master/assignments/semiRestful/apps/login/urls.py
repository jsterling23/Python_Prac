from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process_log_data', views.process_log_data, name='process_log_data'),
]
