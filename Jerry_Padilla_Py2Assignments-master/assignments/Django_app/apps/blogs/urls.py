from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_blog/$', views.new_blog, name='new_blog'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<number>\d+)/$', views.show, name='show'),
    url(r'^(?P<number>\d+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<number>\d+)/delete/$', views.destroy, name='destroy')
]
