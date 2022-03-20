import api
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ColorSerializer, NoteSerializer, TagColorSerializer, TagNoteSerializer, TagSerializer
from notesb.models import Color, Note, Tag, TagColor, TagNote

from api import serializers

from django.db.models import Q

from django.db import connection

from django import db


def executeSQL(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        db.connections.close_all()


@api_view(['POST'])
def getRoutes(request):
    routes = [
        {'POST': '/api/note/'}
    ]
    return Response(routes)


# notes
@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.raw(
        "SELECT * FROM notesb_note LEFT JOIN notesb_tagnote ON noteID = [notesb_note].id;")
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def filterNotes(request, filterSearch, tagNoteID):
    try:
        query = f"SELECT * FROM notesb_note WHERE (tagID LIKE '{tagNoteID}') AND (title LIKE '%{filterSearch}%' OR description LIKE '%{filterSearch}%');"
        notes = Note.objects.raw(query)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    except Note.DoesNotExist:
        return Response('Note not found.')
    
    
    
@api_view(['GET'])
def filterNotesTitleDesc(request, filterSearch):
    try:
        query = f"SELECT * FROM notesb_note WHERE (title LIKE '%{filterSearch}%' OR description LIKE '%{filterSearch}%');"
        notes = Note.objects.raw(query)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    except Note.DoesNotExist:
        return Response('Note not found.')
    
    
@api_view(['GET'])
def filterTagID(request, tagNoteID):
    try:
        query = f"SELECT * FROM notesb_note WHERE (tagID LIKE '{tagNoteID}');"
        notes = Note.objects.raw(query)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    except Note.DoesNotExist:
        return Response('Note not found.')


@api_view(['POST'])
def insertNote(request):
    serializer = NoteSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request, pk):
    deleteTagNote(pk)
    Note.objects.get(id=pk).delete()
    return Response('Note has been deleted.')


@api_view(['DELETE'])
def deleteAllNotes(request):
    Note.objects.all().delete()
    return Response('All notes got deleted.')


@api_view(['POST'])
def updateNote(request, pk):
    serializer = NoteSerializer(data=request.data)
    if(serializer.is_valid()):
        pk = pk.replace('-', '')
        query = f"UPDATE notesb_note SET tagID = '{serializer.data['tagID']}', description = '{serializer.data['description']}', title ='{serializer.data['title']}', modifyDate = DATETIME('now'), image = '{serializer.data['image']}' WHERE id LIKE '{pk}';"
        #Note.objects.filter(id=pk).update(description = serializer.data['description'], title = serializer.data['title'], modifyDate = serializer.data['modifyDate'], image = serializer.data['image'])
        executeSQL(query=query)
    else:
        print(serializer.errors)

    return Response(request.data)


# tag notes
@api_view(['GET'])
def getTagNote(request, pk):
    try:
        tagNote = TagNote.objects.get(noteID=pk)
        serializer = TagNoteSerializer(tagNote, many=False)
        return Response(serializer.data)
    except TagNote.DoesNotExist:
        return Response('Element not found.')


@api_view(['POST'])
def insertTagNote(request):
    serializer = TagNoteSerializer(data=request.data)
    if(serializer.is_valid()):
        deleteTagNote(serializer.validated_data['noteID'])
        serializer.save()

    return Response(request.data)


def deleteTagNote(idNote):
    TagNote.objects.filter(noteID=idNote).delete()


# colors
@api_view(['GET'])
def getColors(request):
    colors = Color.objects.all()
    serializer = ColorSerializer(colors, many=True)
    return Response(serializer.data)


# tags
@api_view(['GET'])
def getTags(request):
    tags = Tag.objects.raw("SELECT [notesb_tag].* FROM notesb_tag;")
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTag(request, pk):
    pk = pk.replace('-', '')
    query = f'SELECT * FROM notesb_tag WHERE [notesb_tag].id = "{pk}";'
    tag = Tag.objects.raw(query)
    serializer = TagSerializer(tag, many=True)
    return Response(serializer.data[0])


@api_view(['POST'])
def insertTag(request):
    serializer = TagSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTag(request, pk):
    Tag.objects.get(id=pk).delete()
    return Response('Tag has been deleted.')


@api_view(['POST'])
def updateTag(request, pk):
    serializer = TagSerializer(data=request.data)
    if(serializer.is_valid()):
        pk = pk.replace('-', '')
        query = f"UPDATE notesb_tag SET name = '{serializer.data['name']}', colorID =  '{serializer.data['colorID']}' WHERE id LIKE '{pk}';"
        #Note.objects.filter(id=pk).update(description = serializer.data['description'], title = serializer.data['title'], modifyDate = serializer.data['modifyDate'], image = serializer.data['image'])
        executeSQL(query=query)
    return Response(request.data)


# tag color
@api_view(['POST'])
def insertTagColor(request):
    serializer = TagColorSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateTagColor(request, pk):
    serializer = TagColorSerializer(data=request.data)
    if(serializer.is_valid()):
        TagColor.objects.filter(id=pk).update(
            colorID=serializer.data['colorID'], tagID=serializer.data['tagID'])

    return Response(request.data)


@api_view(['GET'])
def getTagColors(request):
    tagColors = TagColor.objects.all()
    serializer = TagColorSerializer(tagColors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTagColor(request, pk):
    tagColor = TagColor.objects.get(id=pk)
    serializer = TagColorSerializer(tagColor, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTagColor(request, pk):
    TagColor.objects.get(tagID=pk).delete()
    return Response('Tag Color has been deleted.')
