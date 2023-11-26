from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from registration.forms import SignUpForm

# Create your views here.

def top(request):
  return render(request, "registration/top.html")

class SignUpView(CreateView):
  form_class = SignUpForm
  success_url = reverse_lazy('login')
  template_name = "registration/signup.html"
