from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from notes.models import Note
from notes.serializers.note import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [AllowAny, ]
