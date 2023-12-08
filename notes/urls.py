from django.urls import path

from . import views

urlpatterns = [
    path('list', views.NotesListView.as_view(), name="notes.list"),
    path('<int:pk>/', views.NotesDetailView.as_view(), name="notes.detail"),
    path('create', views.NotesCreateView.as_view(), name="notes.create"),
    path('<int:pk>/edit', views.NotesUpdateView.as_view(), name="notes.edit"),
    path('<int:pk>/delete', views.NotesDeleteView.as_view(), name="notes.delete"),
]