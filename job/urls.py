from django.contrib import admin
from django.urls import path,include
from. import views
from . import api

app_name='jobs'

urlpatterns = [
    path('',views.Joblist,name="job_listt" ),
    path('add',views.add_job,name="add_jobb" ),
    path('<str:slug>',views.jobdetails,name="job_detail" ),
    path('api/list',api.joblistapi,name="joblistapi" ),
    path('api/list/<int:id>',api.joplistapiid,name="joplistapiid" ),
    ]
 
