from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from.models import Place
from.models import Team
#
# def demo(request):
#     return HttpResponse("home")
# def about(request):
#     return render(request,'about.html')
# def contact(request):
#     return HttpResponse("contact")
# def thanks(request):
#     return HttpResponse("thanks")


def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'results':obj1})
