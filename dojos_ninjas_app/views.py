from django.shortcuts import render, redirect, HttpResponse
from dojos_ninjas_app.models import *

# Create your views here.

def index(request):
    context = {
        'dojo_all': Dojo.objects.all(),
        'ninja_all': Ninja.objects.all
    }
    return render (request,"index.html", context)

def add_dojo(request):
    form_name = request.POST['name']
    form_city = request.POST['city']
    form_state = request.POST['state']
    form_desc = request.POST['desc']
    Dojo.objects.create(name = form_name, city = form_city, state = form_state, desc = form_desc)
    return redirect ('/')

def add_ninja(request):
    dojo = request.POST['dojo']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    Ninja.objects.create(dojo_id = dojo, first_name = first_name, last_name = last_name)
    return redirect('/')
    
    

    
    