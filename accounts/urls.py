from django.urls import path
from .views import signup, user_login, upload_file
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', upload_file, name='upload_file'),
]