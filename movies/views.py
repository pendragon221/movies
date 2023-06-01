from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .forms import RegisterForm


class LoginView(LoginView):
    next_page = reverse_lazy("movies:index")

class LogoutView(LogoutView):
    next_page = reverse_lazy("movies:index")

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


