from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process_purchase/$', views.process_purchase, name='process_purchase'),
    url(r'^process_purchase/checkout/$', views.checkout, name='checkout'),
    url(r'^clear_cart/$', views.clear_cart, name='clear_cart'),
]
