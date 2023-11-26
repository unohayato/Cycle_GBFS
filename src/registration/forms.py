from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm,PasswordResetForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.conf import settings

User = get_user_model()


class CustomFormBase(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(CustomFormBase, self).__init__(*args, **kwargs)
        

class CustomLoginForm(CustomFormBase, AuthenticationForm):
    pass

class CustomPasswordChangeForm(CustomFormBase, PasswordChangeForm):
    pass

class CustomPasswordResetForm(CustomFormBase, PasswordResetForm):
    pass


class CustomSignUpForm(CustomFormBase, UserCreationForm):
  class Meta:
    model = User
    fields = ["username", "email", "password1", "password2"]
    
  def save(self, commit=True):
    user = super().save(commit=False)
    user.email = self.cleaned_data["email"]
    user.save()
    return user