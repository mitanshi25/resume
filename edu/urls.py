from django.urls import path
from . import views
urlpatterns =[
path("experience/",views.skill, name= "experience")
]