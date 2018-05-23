from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^thought_form$', views.thought_form, name='thought_form'),
    url(r'^add_thought$', views.add_thought, name='add_thought'),
    url(r'^results$', views.results, name='results'),
]
