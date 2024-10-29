from django.shortcuts import render, get_object_or_404
from .models import Collec
# Create your views here.
def about(request):
    return render(request, 'collec_management/about.html')

def collection_detail(request, id):
    collection = get_object_or_404(Collec, id=id)
    return render(request, 'collec_management/collection_detail.html', {'collection': collection})
