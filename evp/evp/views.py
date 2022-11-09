from django.shortcuts import render, redirect

from django.contrib.auth import authenticate,login
from app.models import Usercreateform

def Master(request):
    return render(request, 'master.html')

def Masterform(request):
    return render(request, 'masterform.html')


def Masterwithouthero(request):
    return render(request, 'masterwithouthero.html')

def Masterwithouthero(request):
    return render(request, 'masterwithouthero.html')

def Index(request):
    return render(request,'index.html')

def Indexform(request):
    return render(request,'indexform.html')

def Form(request):
    return render(request,'form.html')


def signup(request):
    if request.method =='POST':
        form = Usercreateform(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )
            login(request,new_user)
            return redirect('indexform')
    else:
        form = Usercreateform()

    context = {
        'form': form,
    }
    return render(request,'registration/signup.html',context)

    