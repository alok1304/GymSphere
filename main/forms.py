from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EnquiryForm(forms.ModelForm):
    class Meta:
        model =models.Enquiry
        fields= ('full_name','email','location','details')


class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
       model =User
       fields= ('username','email','password1','password2')


class WorkoutForm(forms.Form):
    goal = forms.ChoiceField(choices=[
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('strength', 'Strength Training')
    ])