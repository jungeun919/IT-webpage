from django.urls import path
from .views import *

urlpatterns = [
    path('', vote_list, name="vote_list"),
    path('<int:question_id>', vote_detail, name="vote_detail"),
    path('vote/', vote, name="vote"),
    path('vote_result/<int:question_id>/', vote_result, name="vote_result"),
    path('q_register/', q_register, name="q_register"),
    path('q_delete<int:question_id>', q_delete, name="q_delete"),
    path('c_register/', c_register, name="c_register"),
    path('c_delete<int:choice_id>', c_delete, name="c_delete"),
]