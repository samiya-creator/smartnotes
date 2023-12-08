from django.shortcuts import render
from .models import Notes
from django.http import Http404, HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin

class NotesCreateView(CreateView):
    model =Notes
    form_class = NotesForm
    success_url = '/notes/list'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/notes/list'
    
class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/notes/list'
    template_name = 'notes/notes_delete.html'
    
class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    login_url = '/admin'
    
    def get_queryset(self):
        return self.request.user.notes.all()
    
class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'