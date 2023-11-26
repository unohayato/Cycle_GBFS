from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView

from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView
from .forms import CustomLoginForm, CustomSignUpForm, CustomPasswordChangeForm, CustomPasswordResetForm

# Create your views here.

class CustomLoginView(LoginView):
  form_class = CustomLoginForm

class CustomPasswordChangeView(PasswordChangeView):
  form_class = CustomPasswordChangeForm
    
class CustomPasswordResetView(PasswordResetView):
  form_class = CustomPasswordResetForm

class CustomSignUpView(CreateView):
  form_class = CustomSignUpForm
  success_url = reverse_lazy('login')
  template_name = "registration/signup.html"

def top(request):
  return render(request, "registration/top.html")