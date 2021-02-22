from django.urls import path
from .views import *

urlpatterns = [
    path('', vote_list, name="vote_list"),
    path('<int:question_id>', vote_detail, name="vote_detail"),
    path('vote/', vote, name="vote"),
    path('vote_result/<int:question_id>/', vote_result, name="vote_result"),
]