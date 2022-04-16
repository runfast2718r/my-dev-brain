from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_story_id>/', views.detail, name='detail'),
    path('createForm/', views.createForm, name='createForm'),
    path('createStory/', views.createStory, name='createStory')
]
