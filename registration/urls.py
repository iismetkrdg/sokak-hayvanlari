from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
   #auth pages
   path("registration/login/",views.login_request,name="login"),
   path("register",views.register_request,name="register"),
   path("logout",views.logout_request,name="logout"),

   #email verification
   path("tokensend",views.token_send,name="tokensend"),
   path("success",views.success,name="success"),
   path("verify/<auth_token>",views.verify,name="verify"),
   
   #hata sayfası
   path("error",views.error_page,name="error"),

   #şifre sıfırla
   path("reset_password",auth_views.PasswordResetView.as_view(),name="reset_password"),
   path("reset_password_sent",auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
   path("reset/<uidb64>/<token>",auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
   path("reset_password_complete",auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),

]
