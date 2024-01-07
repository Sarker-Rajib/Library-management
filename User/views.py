from django.shortcuts import render
from django.views.generic import FormView
from .forms import CreateUserForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages

# Create your views here.
class CreateUser(FormView):
    form_class = CreateUserForm
    template_name = 'user/register-form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid.")
        return super().form_invalid(form)

class UserLoginView(LoginView):
    template_name = 'user/login-form.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
class UserLogOUt(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')
    