from django.urls import path
from .views import *

urlpatterns = [
    path('', board, name="board"),
    path('<str:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
    path('comment_new/<str:post_id>', comment_new, name='comment_new'),
    path('update/comment_new/<str:comment_id>', comment_update, name='comment_update'),
    path('delete/comment_new/<str:comment_id>', comment_delete, name='comment_delete'),
]