from django.urls import path, include
from . import views
app_name = 'Entrance'
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),#トップページへのパス
    path('login/', views.Login.as_view(), name="login"),#ログインページへのパス
]