from django.urls import path 
from apprevision import views


urlpatterns=[
    path('',views.users,name='users'),

]