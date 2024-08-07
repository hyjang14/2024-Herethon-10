# accounts/urls.py

from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
    # 회원가입, 회원정보 수정, 로그인, 로그아웃
    path('', views.base, name='base'), 
    path('signup/', views.signup, name='signup'),
    path("user_update/<int:id>/", views.user_update, name="user_update"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    # 회원가입 성공
    path('joinclear/', views.joinclear, name='joinclear'), 

    # 마이페이지
    path('my_page/<int:id>/', views.my_page, name='my_page'),
]