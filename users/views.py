from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from users.forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from users.models import User


class UserRegistrationView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Поздравляем! Вы успешно зарегестрировались!'

    def get_context_data(self, **kwargs):
        context = super(UserRegistrationView, self).get_context_data(**kwargs)
        context['title'] = 'Страница Регистрации'
        return context


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('structure:index')


def logout_view(request):
    logout(request)
    form = UserLoginForm
    return render(request, 'users/login.html', {'form': form})


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['title'] = 'Личный кабинет'
        return context

    def get_success_url(self):
        return reverse_lazy('users:profile', kwargs={'pk': self.object.pk})
