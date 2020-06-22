from django.shortcuts import render, get_object_or_404
from django.urls import reverse

def index(request):
    template_name = 'baseCSS/index.html'
    context = {}
    return render(request, template_name, context)
