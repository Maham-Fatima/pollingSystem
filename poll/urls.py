from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.getQuestion, name='question'),
    path('<int:question_id>/vote/', views.giveVote, name='vote'),
    path('<int:question_id>/result/', views.getVoteCount, name='result'),
]