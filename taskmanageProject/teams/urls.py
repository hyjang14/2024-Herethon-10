from django.urls import path
from . import views

app_name = "teams"

urlpatterns = [
    # 메인 페이지
    path('', views.team_list, name='team_list'),
    
    # 팀
    path('team_create/', views.TeamCreateView.as_view(), name='team_create'),
    path('team_update/<int:id>/', views.team_update, name='team_update'),
    path('team_delete/<int:team_id>/', views.team_delete, name='team_delete'),

    # 팀 상세페이지
    path('team_detail/<int:id>/', views.team_detail, name='team_detail'),

    # 팀 좋아요
    path('<int:team_id>/likes/', views.likes, name='likes'),

    # 할 일
    path('task_create/<int:id>/', views.task_create, name='task_create'),
    path('task_update/<int:id>/', views.task_update, name='task_update'),
    path('task_delete/<int:id>/', views.task_delete, name='task_delete'),
]