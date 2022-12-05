from django.shortcuts import render
from cleansite.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.template.loader import render_to_string
from clean_site import settings
from cleansite import popforms
from django.http import HttpResponse


# Create your views here.

def index(request):
    context = {}
    form = ContactForm()
    context['form'] = form
    return render(
        request,
        'index.html',
        context = context
    )

def mainform(request):
    context = {}
    if request.method =='POST':
        form = popforms.ContactFormPoop(request.POST)
        if form.is_valid():
            context['form'] = form.cleaned_data
            email_form = form.cleaned_data['email']
            if str(email_form) == '':
                email_form = 'Пользователь не оставил е-майл'
            text = (f'Здравствуйте!\n\nНовая заявка с сайта Клининг Порядок\n\nИмя: {form.cleaned_data["namepops"]}\nНомер телефона: {form.cleaned_data["numbers"]}\nПочтовый адрес: {email_form}')
            send_mail('Заявка с сайта', text, 'orderclean@mail.ru', ['mersbenza@mail.ru', 'nonamers1336@mail.ru'], fail_silently=False)
            context = {'succes': '1'}
    form.cleaned_data
    return HttpResponse('успешно')

def indexform(request):
    context = {}
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            context['form'] = form
            text = (f'Здравствуйте!\n\nНовая заявка с сайта Клининг Порядок\n\nИмя: {form.cleaned_data["name"]}\nНомер телефона: {form.cleaned_data["number"]}')
            send_mail('Заявка с сайта', text, 'orderclean@mail.ru', ['mersbenza@mail.ru', 'nonamers1336@mail.ru'], fail_silently=False)
            context = {'succes' : '1'}
    form.cleaned_data
    return HttpResponse('успешно')

def useragree(request):
    return render(
        request,
        'useragree.html',
    )