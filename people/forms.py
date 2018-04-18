from django import forms
from countries.models import Country
from people.models import Person

class RegisterForm(forms.Form):
  first_name = forms.CharField(label="First Name:")
  nacionality = forms.ModelMultipleChoiceField(queryset=Country.objects.all())
  father = forms.ModelChoiceField(required=False, queryset=Person.objects.all())

class RegisterFormModel(forms.ModelForm):

  def __init__(self, fathers, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['father'].queryset = fathers

  class Meta:
    model = Person
    fields = ['first_name', 'nacionality', 'father']