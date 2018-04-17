from django import forms

class RegisterForm(forms.Form):
  first_name = forms.CharField(label="First Name:")