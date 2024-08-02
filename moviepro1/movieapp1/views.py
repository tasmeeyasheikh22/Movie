from django.shortcuts import render,redirect
from .forms import MovieForm
from .models import models

# Create your views here.
def addview(request):
    form = MovieForm()
    if request.method=="POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"movieapp1/add.html",{"form":form})

def viewsview(request):
    obj = MovieForm.objects.all()
    return render(request,"movieapp1/views.html",{"mov":obj})

def updateview(request,id):
    obj= MovieForm.objects.get(id=id)
    form = MovieForm(instance=obj)
    if request.method=="POST":
        form = MovieForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/a1/av/")
    return render(request,"movieapp1/add.html",{})

def deleteview(request,ud):
    obj = MovieForm.objects.get(id=ud)
    obj.delete()
