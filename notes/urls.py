from django.urls import path

from . import views

urlpatterns = [
    path('list', views.NotesListView.as_view(), name="notes.list"),
    path('<int:pk>/', views.NotesDetailView.as_view(), name="notes.detail"),
    path('create', views.NotesCreateView.as_view(), name="notes.create"),
]