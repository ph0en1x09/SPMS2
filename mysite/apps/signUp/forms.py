from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from mysite.models import Member

class DateInput(forms.DateInput):
	input_type = 'date'

class CreateUserForm(UserCreationForm):
    age = forms.DateField(widget = DateInput)
    gender = forms.CharField(max_length = 100)

    class Meta:
        model = Member
        fields = ['name', 'first_name', 'last_name', 'age', 'gender', 'email', 'password1', 'password2']
