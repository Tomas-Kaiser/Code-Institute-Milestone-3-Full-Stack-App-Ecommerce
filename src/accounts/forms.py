from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
   password1   = forms.CharField(label='Password', widget=forms.PasswordInput)
   password2   = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

   class Meta:
      model = User
      fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

   def clean_email(self):
      email = self.cleaned_data.get('email')
      username = self.cleaned_data.get('username')
      qs = User.objects.filter(email=email).exclude(username=username)
      if qs.exists():
         raise forms.ValidationError("This email already exists!")
      return email
