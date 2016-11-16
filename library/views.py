from django.shortcuts import render
from django.views.generic.edit  import  CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
# Create your views here.


class Home(TemplateView):
    template_name = "index.html"


