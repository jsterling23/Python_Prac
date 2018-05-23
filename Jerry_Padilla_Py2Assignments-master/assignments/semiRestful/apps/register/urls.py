from django.conf.urls import url
from . import views


# register urls


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.process_reg_data, name='process_reg_data'),
]
