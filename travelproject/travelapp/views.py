from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from . models import Team

# Create your views here.
def demo(request):
    obj=Place.objects.all()


    return render(request,"index.html",{'result':obj})


def demo(request):
    obj=Team.objects.all()
    return render(request,"index.html",{"res":obj})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     div=x/y
#     mult=x*y
#     return render(request, "result.html", {'add': add,'sub':sub,'div':div,'mult':mult})

#     return render(request, "result.html", {'add':add})
#
# def subtraction(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     sub=x-y
#     return render(request, "result.html", {'sub': sub})
#
# def divition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     div=x/y
#     return render(request, "result.html",{'div':div})
#
# def multi(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     mul=x*y
#     return render(request,"result.html",{'mul':mul})