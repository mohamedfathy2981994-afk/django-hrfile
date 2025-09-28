from datetime import datetime, timezone
from django.views.generic import ListView, DetailView
from .models import maindata
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from io import BytesIO
from workfiles.models import maindata

def home(request):
    return render(request, 'workfiles/home.html')

class MaindataListView(ListView):
    model = maindata
    template_name = 'workfiles/maindata_list.html'
    context_object_name = 'maindatas'

class MaindataDetailView(DetailView):
    model = maindata
    template_name = 'workfiles/maindata_detail.html'
    context_object_name = 'maindata'


def generate_html(request, pk):
    maindata_instance = get_object_or_404(maindata, pk=pk)
    context = {
        'maindata': maindata_instance,
    }
    return render(request, 'workfiles/generate_html.html', context)
