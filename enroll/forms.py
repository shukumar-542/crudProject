from pyexpat import model
from django import forms
from .models import User

class studentRegistration(forms.ModelForm):
      class Meta:
            model = User
            fields = ['name','email','password']

            widgets ={
                  'name':forms.TextInput(attrs={'class':'form-control'}),
                  'email':forms.EmailInput(attrs={'class':'form-control'}),
                  'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'})

            }