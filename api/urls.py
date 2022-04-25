from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.getRoutes),
    
    #notes
    path('notes/', views.getNotes),
    path('notes/id=<str:pk>/', views.getNote),
    path('createNote/', views.insertNote),
    path('deleteNote/id=<str:pk>/', views.deleteNote),
    path('updateNote/id=<str:pk>/', views.updateNote),
    path('filterNote/filterSearch=<str:filterSearch>&tagID=<str:tagNoteID>/', views.filterNotes),
    path('filterNote/filterSearch=/', views.getNotes),
    path('filterNote/filterSearch=<str:filterSearch>/', views.filterNotesTitleDesc),
    path('filterNote/tagID=<str:tagNoteID>/', views.filterTagID),
    
    #tagNote
    path('tagNote/noteID=<str:pk>/', views.getTagNote),
    path('insertTagNote/', views.insertTagNote),
    
    #colors
    path('colors/', views.getColors),
    
    
    #tags
    path('tags/', views.getTags),
    path('tags/id=<str:pk>/', views.getTag),
    path('createTag/', views.insertTag),
    path('deleteTag/id=<str:pk>/', views.deleteTag),
    path('updateTag/id=<str:pk>/', views.updateTag),
    
    
    #tag colors
    path('tagColors/', views.getTagColors),
    path('tagColors/tagID=<str:pk>/', views.getTagColor),
    path('createTagColor/', views.insertTagColor),
    path('updateTagColor/id=<str:pk>/', views.updateTagColor),
    path('deleteTagColor/tagID=<str:pk>/', views.deleteTagColor),
    
    #Debug
    path('deleteAllNotes/', views.deleteAllNotes)
]