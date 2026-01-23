from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def home(request):
    #return HttpResponse("Hi. This is my first view!")
    return render(request, "home.html")

# Список активних столиків
def tables_list(request):
    tables = Table.objects.filter(is_active=True)
    context = {"tables": tables}
    return render(request,"tables_list.html",context)