from django import forms
from django.forms import widgets
from .models import Curd

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Curd
        fields = ['name', 'email', 'password']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'id':'nameid'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'id':'emailid'}),
            'password':forms.PasswordInput(attrs={'class':'form-control', 'id':'passid', 'autocomplete':'on'}),
        }