from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^kicked/$', views.kicked, name='kicked'),
]
