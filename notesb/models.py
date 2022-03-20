from django.db import models
import uuid

class Note(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=256)
    description = models.TextField(null = True, blank = True)
    createDate = models.DateTimeField(null=True, blank=True)
    modifyDate = models.DateTimeField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    tagID = models.TextField(null=True, blank=True)

class Color(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.TextField(max_length=128)
    hexCode = models.CharField(max_length=32)
    
    
class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.TextField(max_length=128)
    colorID = models.TextField(null=True, blank=True)
    
    
class TagColor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    tagID = models.UUIDField(null=False)
    colorID = models.TextField(null=True, blank=True)
    

class TagNote(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    tagID = models.UUIDField(null=True)
    noteID = models.UUIDField(null=True)