from rest_framework import serializers
from notesb.models import Color, Note, Tag, TagColor, TagNote

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
        

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        
        
class TagColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagColor
        fields = '__all__'
        
        
class TagNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagNote
        fields = '__all__'