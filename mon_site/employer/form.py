
from django import forms
from .models import *

class EmployerForm(forms.ModelForm):
    class Meta:
        model=Employer
        fields= ['nom','email','poste','salaire']
        widgets={
            'nom':forms.TextInput(attrs={
                'class':'input w-full',
                'placeholder':'Nom'
            }),
            'email':forms.EmailInput(attrs={
                'class':'input w-full',
                'placeholder':'Email'
            }),
            'poste':forms.TextInput(attrs={
                'class':'input w-full',
                'placeholder':'Poste'
            }),
            'salaire':forms.TextInput(attrs={
                'class':'input w-full',
                'placeholder':'Salaire'
            })
            
            
            
        }
            
         