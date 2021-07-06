from django.urls import path
from django.contrib import admin


from . import views


urlpatterns = [
    #path('<team_id>/', views.index, name='index'),
    path('', views.index, name='index'),
    
]