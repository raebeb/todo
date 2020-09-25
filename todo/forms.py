from django import forms
from django.forms.widgets import TextInput 

class TodoForm(forms.Form):
    text = forms.CharField(max_length=50, required=False,
            widget=forms.TextInput( attrs={
                'class': 'form-control',
                'placeholder': 'Escribe algo para hacer hoy',
                'aria-label': 'Todo', 
                'aria-describedby': 'add-btn' 
            })
            )