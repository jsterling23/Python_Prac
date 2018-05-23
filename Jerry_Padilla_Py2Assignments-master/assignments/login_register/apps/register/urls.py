from django.conf.urls import url
from . import views

# Register paths


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^data/$', views.process_data, name='process_data'),
]
