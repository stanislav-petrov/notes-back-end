import re

from notes.models import Note
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):
    content = serializers.CharField()

    def validate(self, attrs):
        content = attrs.get('content')

        # Validate the string length is no more than 30 chars
        if len(content) > 30:
            raise serializers.ValidationError("Having content greater than 30 chars is not allowed!")

        pattern = r"[-!$%\^#&*()_+|~=`{}\[\]:\";'<>?,.\/]+"
        is_not_valid = bool(re.findall(pattern, content))

        if is_not_valid:
            raise serializers.ValidationError("Non-supported chars found")

        return attrs

    class Meta:
        model = Note
        fields = ('content', )
