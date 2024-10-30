from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from collec_management.forms import CollecForm
from .models import Collec
# Create your views here.
def about(request):
    return render(request, 'collec_management/about.html')

def collection(request, id):
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
        return HttpResponseRedirect(reverse('collection', args=[collection.id]))
    else :
        form=CollecForm()
    return render(request , 'collec_management/formulaire.html' , {"form" : form})


def delete ( request , collec_id ) :
    collec = get_object_or_404 ( Collec , pk = collec_id )
    if request.method == "POST" :
        collec.delete()
        return redirect ("all")
        
    return render (request, "collec_management/collec_delete.html" ,
                   {"collec":collec})

def check_save(form):
    if form.is_valid():
        collec=form.save(commit=False)
        collec.save()
    return collec.id

def change(request, collec_id):
    collec=get_object_or_404(Collec, pk=collec_id)
    if request.method =="POST":
        form=CollecForm(request.POST, instance=collec)
        collecModif_id=check_save(form)
        return redirect("collection", id=collecModif_id)
    else:
        form=CollecForm(instance=collec)
    return render(request, "collec_management/collec_modifier.html"
                  , {"form": form})