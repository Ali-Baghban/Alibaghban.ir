from django.shortcuts import render
from django.shortcuts import redirect
from contact_us import models
from django.contrib import messages

def message_send(request):
    if request.method == 'POST':
        name        = request.POST.get('name', 'Not provided')
        email       = request.POST.get('email', 'Not provided')
        subject     = request.POST.get('subject', 'Not provided')
        message     = request.POST.get('message', 'Not provided')

        if len(name) < 2:
            messages.error(request, "There are some Error in sending the message !")
            return redirect('home')
        else:
            obj         = models.Message.objects.create(name=name, email=email, subject=subject, message=message)
            obj.save()
            messages.success(request, "Your message has been sent successfully")
            return redirect('home')
        
    messages.error(request, "There are some Error in sending the message !")
    return redirect('home')