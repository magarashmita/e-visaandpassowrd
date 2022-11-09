from django.shortcuts import render


# Create your views here.
def Master(request):
    return render(request,'master.html')

def Masterwithouthero(request):
    return render(request,'masterwithouthero.html')
