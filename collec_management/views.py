from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from collec_management.forms import CollecForm
from .models import Collec
# Create your views here.
def about(request):
    return render(request, 'collec_management/about.html')

def collection_detail(request, id):
    try:
        collection=Collec.objects.get(pk=id)
    except Collec.DoesNotExist:
        raise Http404("La collection n'existe pas")
    return render(request, 'collec_management/collection_detail.html', {'collection': collection})

def all(request):
    collections=Collec.objects.all()
    return render(request, "collec_management/colleclist.html", {"collections":collections})

def new (request) :
    if request.method =='POST':
        form =CollecForm(request.POST)
        if form.is_valid():
            collection =form.save(commit=False)
            collection.save()
        return HttpResponseRedirect(reverse('collection_detail', args=[collection.id]))
    else :
        form=CollecForm()
    return render(request , 'collec_management/formulaire.html' , {"form" : form})
    