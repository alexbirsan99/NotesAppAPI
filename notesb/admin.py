from django.contrib import admin

from .models import Note, Color, TagColor, Tag, TagNote

admin.site.register(Note)
admin.site.register(Color)
admin.site.register(TagColor)
admin.site.register(Tag)
admin.site.register(TagNote)