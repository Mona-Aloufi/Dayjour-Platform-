from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
 path('', views.home),
 path('en/login/',views.login_view, name='login'),
 path('en/signup/',views.signin_view, name='signup'),
 path('dashboard',views.dashboard, name='dashboard'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
