from django.shortcuts import render
from app.models import Visaform


# Create your views here.
def Master(request):
    return render(request,'master.html')


def Index(request):
    visaform = Visaform.objects.alt()

    context={
        'visaform':visaform,
    }
# return render(request,'index.htm\l',context)
