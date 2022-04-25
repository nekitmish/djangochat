from rest_framework import serializers

from chats.models import Chat
from messages.services import AllChatMessagesRetriever
from users.api.serializers import UserSerializer


class ChatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = [
            'companion',
        ]


class ChatRetrieveSerializer(serializers.ModelSerializer):
    companion = UserSerializer()

    class Meta:
        model = Chat
        fields = [
            'companion',
            'is_archived',
            'is_unread',
        ]


class ChatListSerializer(serializers.ModelSerializer):
    companion = UserSerializer()
    last_message = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Chat
        fields = [
            'id',
            'companion',
            'is_archived',
            'is_unread',
        ]

    def get_last_message(self, chat):
        all_messages_retriever = AllChatMessagesRetriever(chat)
        all_messages = all_messages_retriever()
        return all_messages.first()
