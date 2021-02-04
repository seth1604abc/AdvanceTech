from django.shortcuts import render
from .models import *

def index(request):
    plants = Plant.objects.all()
    units = Unit.objects.all()
    context = {'plants': plants, 'units': units}
    return render(request, 'index.html', context)

