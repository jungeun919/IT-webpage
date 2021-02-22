from django.urls import path
from .views import *

urlpatterns = [
    path('', book_list, name="book_list"),
    path('add/', add, name="add"),
    path('book_create/', book_create, name="book_create"),
    path('book_delete/<str:id>', book_delete, name="book_delete"),
]