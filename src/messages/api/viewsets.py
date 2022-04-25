from rest_framework.permissions import IsAuthenticated

from djangochat.api.viewsets import DefaultCreateModelViewSet
from messages.api import serializers
from messages.models import Message
from messages.services import MessageCreator


class MessageViewSet(DefaultCreateModelViewSet):
    serializer_class = serializers.MessageSerializer
    serializer_action_classes = {
        'create': serializers.MessageCreateSerializer,
    }
    queryset = Message.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        message_creator = MessageCreator(
            sender=self.request.user,
            **serializer.validated_data,
        )
        return message_creator()
