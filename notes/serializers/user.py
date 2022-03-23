from rest_framework import serializers

from notes.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ('email', 'username', )
