from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import contactForm
from django.template import loader
from django.conf import settings

# Create your views here.
def send_email(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            name =  form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            subject = 'Message from MySite'
            Email = form.cleaned_data['Email']
            emailTo = [settings.EMAIL_HOST_USER]
            message = 'name = %s, message = %s' %(name, comment)

            try:
                send_mail(subject, message, Email, emailTo, fail_silently=False)

            except BadHeaderError:
                return HttpResponse('invalide header')

            return redirect('contact:send_success')


    
    else:
        form = contactForm()

    context = {
        'form' : form
    }

    return render(request, 'contact/contact.html', context)
    

def send_success(request):
   template = loader.get_template('contact/success.html')
   return HttpResponse(template.render({"active_tab":"success","request":request})) 