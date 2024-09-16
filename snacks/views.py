
# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView, 
)   

from .models import Pattern
# CRUD

class PatternCreateView(CreateView):
    template_name = 'patterns/pattern-create.html'
    model = Pattern
    fields = ['name', 'description', 'added_by', 'category', 'more_info']

class PatternListView(ListView):
    template_name = 'patterns/pattern-list.html'
    model = Pattern
    
class PatternDetailView(DetailView):
    template_name = 'patterns/pattern-detail.html'
    model = Pattern
    
class PatternUpdateView(UpdateView):
    template_name = 'patterns/pattern-update.html'
    model = Pattern
    fields = ['name', 'description', 'added_by', 'category', 'more_info']
    
class PatternDeleteView(DeleteView):
    template_name = 'patterns/pattern-delete.html'
    model = Pattern
    success_url = reverse_lazy('pattern_list')
    



