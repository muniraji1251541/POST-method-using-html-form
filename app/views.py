from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def form(request):
    if request.method=='POST':
        tn=request.POST['topic']
        t=Topic.objects.get_or_create(topic_name=tn)[0]
        t.save()
        return HttpResponse('Topic data is submitted successfully')

    return render(request,'form.html')

def form1(request):
    if request.method=='POST':
        
        
        w1=request.POST['topic']
        w2=request.POST['name']
        w3=request.POST['url']
        t=Topic.objects.get_or_create(topic_name=w1)[0]
        t.save()
        w=Webpage.objects.get_or_create(topic_name=t,name=w2,url=w3)[0]
        w.save()
        return HttpResponse('Webpage data is submitted successfully')

    return render(request,'form1.html')

def form2(request):
    if request.method=='POST':
        a1=request.POST['name']
        a2=request.POST['date']
        w=Webpage.objects.get_or_create(name=a1)[0]
        w.save()
        a=Accessrecord.objects.get_or_create(name=w,date=a2)[0]
        a.save()
        return HttpResponse('Accessrecord data is submitted successfully')

    return render(request,'form2.html')