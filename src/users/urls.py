from django.urls import path, include
from users.views import signup, login, logout, delete_account
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accounts/', include('allauth.urls')),  # URLs allauth
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('delete_account/', delete_account, name='delete_account'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
            template_name="registration/password_reset_form.html",
            success_url='/users/password_reset/done/',
            subject_template_name='registration/password_reset_subject.txt'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
            template_name="registration/password_reset_done.html"
         ),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_confirm.html"
         ),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
            template_name="registration/password_reset_complete.html"
         ),
         name='password_reset_complete'),
]