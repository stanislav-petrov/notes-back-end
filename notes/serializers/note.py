
from notes.models import Note
from rest_framework import serializers

from notes.serializers.user import UserSerializer


class NoteSerializer(serializers.ModelSerializer):
    content = serializers.CharField()
    creator = UserSerializer()

    class Meta:
        model = Note
        fields = ('content', 'creator')
