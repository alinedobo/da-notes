from django.urls import path
from .views import NoteList, NoteSingleView

urlpatterns = [
    path('notes/', NoteList.as_view()),
    path('notes/<int:pk>/', NoteSingleView.as_view(), name='note-detail')
]