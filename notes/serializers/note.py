
from notes.models import Note
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):
    content = serializers.CharField()

    class Meta:
        model = Note
        fields = ('content', )
