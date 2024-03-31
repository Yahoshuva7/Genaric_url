from django.shortcuts import render
from django.http import *
# Create your views here.
def virat(request):
    return render(request,'virat.html')
def maxwell(request):
    return HttpResponse('hard hitter')