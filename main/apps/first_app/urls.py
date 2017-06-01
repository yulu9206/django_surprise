from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^form_process$', views.form_process),
    url(r'^surprises$', views.surprises)
      ]
