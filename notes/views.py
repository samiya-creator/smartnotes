from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView
from .forms import NotesForm

class NotesCreateView(CreateView):
    model =Notes
    form_class = NotesForm
    success_url = '/notes/list'
class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    
class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'