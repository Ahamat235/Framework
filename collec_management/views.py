from django.http import HttpResponse, Http404
from django.shortcuts import render
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