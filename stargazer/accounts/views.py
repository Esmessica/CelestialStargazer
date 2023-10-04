from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

# Create your views here.


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    # after sign up for website, revrse them to login page, reverselaze == executes after submit button
    template_name = 'accounts/signup.html'