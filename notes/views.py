from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import NotesForm

class NotesCreateView(CreateView):
    model =Notes
    form_class = NotesForm
    success_url = '/notes/list'
    
class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/notes/list'
    
class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/notes/list'
    template_name = 'notes/notes_delete.html'
    
class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    
class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'