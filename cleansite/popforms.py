from django import forms
from django.shortcuts import render
from django.http import JsonResponse

class ContactFormPoop(forms.Form):
    namepops = forms.CharField(
        min_length = 5,
        widget=forms.TextInput(
        attrs = {'placeholder': 'Ваше имя *'}
    ) )

    
    numbers = forms.CharField(
            widget=forms.TextInput(
            attrs = {'placeholder': 'Ваш номер телефона *'}
        )  
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs = {'placeholder': 'Ваш e-mail адрес'},
        ),
        required=False
    
    
    )

    # numbers.widget.attrs.update({'span':})
    
def pop(request):
    context = {}
    pop_info = ContactFormPoop()
    return ({'namepop': pop_info['namepops'],
            'numberpop': pop_info['numbers'],
            'email': pop_info['email']})
