from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views, forms

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(authentication_form=forms.LoginForm), name='login'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user/<str:username>', views.profile, name='profile'),
    path('user/<str:username>/user_delete/', views.user_delete_view, name='user_delete'),
    #path('user/<str:username>/user_delete/', views.user_delete_view, name='user_delete'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html',
                                                                 email_template_name='password_reset_email.html'),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),

]
