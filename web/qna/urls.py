from django.urls import path
from .views import *

urlpatterns = [
    path('', qna_board, name="qna_board"),
    path('<str:id>', qna_detail, name="qna_detail"),
    path('qna_new/', qna_new, name="qna_new"),
    path('qna_create/', qna_create, name="qna_create"),
    path('qna_edit/<str:id>', qna_edit, name="qna_edit"),
    path('qna_update/<str:id>', qna_update, name="qna_update"),
    path('qna_delete/<str:id>', qna_delete, name="qna_delete"),
    path('comment_new/<str:post_id>', comment_new, name='comment_new'),
    path('update/comment_new/<str:comment_id>', comment_update, name='comment_update'),
    path('delete/comment_new/<str:comment_id>', comment_delete, name='comment_delete'),
]