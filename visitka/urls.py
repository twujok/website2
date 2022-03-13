from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about_me', views.about_me, name='about_me'),
    path('project', views.project, name='project'),
    path('dolboeb', views.dolboeb, name='dolboeb'),
    path('back', views.back, name='back')
]
