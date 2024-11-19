from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView, LoginView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserProfileForm, UserForgotPasswordForm, UserAuthenticationForm, UserPreferencesForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        host = self.request.get_host()
        activation_url = f'http://{host}/users/confirm-email/{uid}/{token}'
        send_mail(
            'Подтверждение адреса электронной почты',
            f'Для подтверждения регистрации пройдите по ссылке {activation_url}',
            EMAIL_HOST_USER,
            [user.email],  # Это поле "Кому" (можно указать список адресов)
            fail_silently=False,  # Сообщать об ошибках («молчать ли об ошибках?»)
        )
        return redirect('users:email_confirmation_sent')


def email_confirmation_sent(request):
    return render(request, 'users/email_confirmation_sent.html')


class UserConfirmEmailView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('users:email_confirmed')
        else:
            return redirect('users:email_confirmation_failed')


def email_confirmed(request):
    return render(request, 'users/email_confirmed.html')


def email_confirmation_failed(request):
    return render(request, 'users/email_confirmation_failed.html')


class UserForgotPasswordView(PasswordResetView):
    """
    Представление по сбросу пароля по почте
    """
    form_class = UserForgotPasswordForm
    template_name = 'users/password_reset.html'
    success_url = reverse_lazy('content:content_list')
    success_message = 'Письмо с инструкцией по восстановлению пароля отправлена на ваш email'
    subject_template_name = 'users/email/new_password_subject_mail.txt'
    email_template_name = 'users/email/new_password_mail.html'


class UserPasswordResetConfirmView(View):
    def get(self, request, uidb64, token, pas):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.set_password(pas)
            user.save()
            return redirect('users:password_confirmed')
        else:
            return redirect('users:password_confirmation_failed')


def password_confirmed(request):
    return render(request, 'users/password_confirmed.html')


def password_confirmation_failed(request):
    return render(request, 'users/password_confirmation_failed.html')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('content:content_list')

    def get_object(self, queryset=None):
        return self.request.user


class PreferencesView(UpdateView):
    model = User
    form_class = UserPreferencesForm
    success_url = reverse_lazy('content:recommended_list')

    def get_object(self, queryset=None):
        return self.request.user


class UserLoginView(LoginView):
    form_class = UserAuthenticationForm
    success_url = reverse_lazy('content:recommended_list')