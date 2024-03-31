from django.shortcuts import render
from django.http import *
def msd(request):
    return render(request,'dhoni.html')
def raina(request):
    return HttpResponse('mr.ipl')
