from django.shortcuts import render
from .models import *
from django.http import HttpResponse


def home(request):
    hero = hero_section.objects.all()
    skill_data = skill_section.objects.all()
    course_data =course_list.objects.all()
    project_data =project_list.objects.all()
    acadamics_data =acadamics_details.objects.all()
    touch_data =get_touch.objects.all()
    foot_data =footer.objects.all()
    skill_icon_feed = skill_icon.objects.all()


    context = {'hero': hero,
               'skill_data': skill_data,
               'course_data': course_data,
               'project_data': project_data,
               'acadamics_data': acadamics_data,
               'touch_data': touch_data,
               'foot_data': foot_data,
               'skill_icon_feed':skill_icon_feed,}
    return render(request,"index.html",context)

def save_form(request):
    context={}
    if request.method == "POST":
        name = request.POST.get("name")
        em = request.POST.get("email")
        sub = request.POST.get("subject")
        msz = request.POST.get("message")
        obj = contact_us(name =name, email = em, subject = sub, message = msz)
        obj.save()
        context['message']=f"Dear {name}, Thanks for your time!"
    return render(request,"saveform.html",context)
        
