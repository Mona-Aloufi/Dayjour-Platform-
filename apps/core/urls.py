from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('en/login/', views.login_view, name='login'),
    path('en/signup/', views.signin_view, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/', views.encrypt_data_view, name='upload_data'),
    path('download/<str:encrypted_file>/', views.download_encrypted_file_view, name='download_encrypted_file'),
     path('trainLocalmodel/', views.trainLocalmodel, name='train_local_model'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]