from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactData

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
                SaveContactData(subject, message, from_email)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'home/contact.html', {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

def SaveContactData(subject, message, from_email):
    contact_data=ContactData()
    contact_data.name=subject
    contact_data.email=from_email
    contact_data.message=subject
    contact_data.save()
    
