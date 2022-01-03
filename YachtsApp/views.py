from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Yacht

# Create your views here.
def index(request):
    all_yachts = Yacht.objects.all()
    context = {
        'all_yachts': all_yachts,
    }
    return render(request, 'YachtsApp/index.html', context)

def booking(request, yacht_id):
    yacht = Yacht.objects.get(pk=yacht_id)
    context = {
        'yacht': yacht
    }
    return render(request, 'YachtsApp/booking.html', context)