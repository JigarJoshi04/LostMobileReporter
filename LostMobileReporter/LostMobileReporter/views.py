from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    print('Home View')
    return render(request,'home.html')