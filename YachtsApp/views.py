from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Yacht

# Create your views here.
def index(request):
    all_yachts = Yacht.objects.all()
    template = loader.get_template('YachtsApp/index.html')
    context = {
        'all_yachts': all_yachts,
    }
    return HttpResponse(template.render(context, request))