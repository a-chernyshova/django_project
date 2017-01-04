from django.conf.urls import url
from django.contrib import admin
from job_skills import views
urlpatterns = [
    url(r'^$', views.index),
]
