from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('mixin/', views.TodoMOMCV.as_view(), name='mixin'),
]