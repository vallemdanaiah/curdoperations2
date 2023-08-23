from django.forms import ModelForm
from django import forms
from .models import Student
class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'},render_value=True)
        }
  