from django.urls import path
from . import views
from .forms import PasswordResetConfirmForm, PasswordResetForm
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.account_register, name="register"),
    path("login/", views.account_login, name="login"),
    path("logout/", views.account_logout, name="logout"),
    path("delete/", views.account_delete, name="delete_account"),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="account/user/password-reset-form.html",
            success_url="password-reset-email-confirm",
            email_template_name="account/user/password-reset-email.html",
            form_class=PasswordResetForm,
        ),
        name="password_reset",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="account/user/password-reset-confirm.html",
            success_url="/account/password-reset-complete/",
            form_class=PasswordResetConfirmForm,
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/password-reset-email-confirm/",
        TemplateView.as_view(template_name="account/user/password-reset-success.html"),
        name="password_reset_done",
    ),
    path(
        "password-reset-complete/",
        TemplateView.as_view(template_name="account/user/password-reset-success.html"),
        name="password_reset_complete",
    ),
    path(
        "change-password/",
        auth_views.PasswordChangeView.as_view(
            template_name="account/user/forgot-password.html", success_url="/"
        ),
        name="change_password",
    ),
]
