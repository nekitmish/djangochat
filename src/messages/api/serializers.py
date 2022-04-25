from rest_framework import serializers

from messages.models import Message
from users.api.serializers import UserSerializer


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'recipient',
            'body',
        ]


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    recipient = UserSerializer()

    class Meta:
        model = Message
        fields = [
            'id',
            'sender',
            'recipient',
            'body',
            'created_at',
        ]
