from rest_framework import viewsets

from notes.models import Note
from notes.serializers.note import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
