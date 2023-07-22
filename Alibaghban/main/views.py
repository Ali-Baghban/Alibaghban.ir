from django.shortcuts import render
from django.http import HttpResponse
from main import models

def home(request):

    main = models.Main.objects.filter(is_chosen=True).first()
    print(main)
    if not main:
        return HttpResponse("Underconstruction ...")
    
    about = models.About.objects.filter(is_chosen=True).first()
    skills= models.Skill.objects.all()
    resume= models.Resume.objects.all()
    certs = models.Certification.objects.all()

    context = {
        'main': main,
        'about' : about,
        'skills':skills,
        'resume':resume,
        

    }
    return render(request, template_name='main/index.html', context=context)