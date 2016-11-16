from django.shortcuts import render
from django.views.generic.edit  import  CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from .form import SearchForm
from .models import Books



class Search(object):
    def get_context_data(self,**kwargs):
        context = super(Search,self).get_context_data(**kwargs)
        context['search_form'] = SearchForm()
        return context

class HomeView(Search, TemplateView):
    template_name = "index.html"



class SearchView(Search,ListView):
    ''' performs search '''
    template_name = "index.html"
    context_object_name = "results"

    def get_queryset(self):
        search = self.request.GET.get('search')
        filter = self.request.GET.get('filter')
        if filter == 'category':
            context = Books.objects.filter(category__name__iexact=search)
        else:
            context = Books.objects.filter(title__contains=search)
        return context

