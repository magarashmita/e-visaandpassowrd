from django import forms
from django.forms import ModelForm
from .models import Visaform


#create a VisaForm
class Visaforms(ModelForm):
    class Meta:
        model = Visaform
        fields = ('Firstname','middlename','Lastname','Gender')

class Passportforms(ModelForm):
    class Meta:
        model = Visaform
        fields = ('Firstname','middlename','Lastname','Gender')