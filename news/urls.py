from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('news/<int:id>/', views.details, name='details'),
    path('category/<str:tag>/', views.category, name='category'),
    path('pdf/<int:id>', views.pdf, name='pdf'),
]
