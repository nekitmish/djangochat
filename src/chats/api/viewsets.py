from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from chats.api import serializers
from chats.api.filtersets import ChatFilter
from chats.api.permissions import IsMyChat
from chats.models import Chat
from chats.services import ChatArchiver
from chats.services import ChatCreator
from chats.services import ChatUnreadMarker
from djangochat.api.viewsets import DefaultModelViewSet
from messages.api.serializers import MessageSerializer
from messages.services import AllChatMessagesRetriever


class ChatViewSet(DefaultModelViewSet):
    permission_classes = [IsAuthenticated]
    filterset_class = ChatFilter
    queryset = Chat.objects.for_viewset().all()
    serializer_action_classes = {
        'create': serializers.ChatCreateSerializer,
        'list': serializers.ChatListSerializer,
        'retrieve': serializers.ChatRetrieveSerializer,
    }

    def get_queryset(self):
        return self.queryset.filter(me=self.request.user)

    @action(detail=True, methods=['POST'], url_path='archive', permission_classes=[IsMyChat])
    def archive(self, request, pk=None):
        chat = self.get_object()
        chat_archiver = ChatArchiver(chat)
        chat = chat_archiver()
        return self.response(chat, 200)

    @action(detail=True, methods=['POST'], url_path='mark-unread', permission_classes=[IsMyChat])
    def mark_unread(self, request, pk=None):
        chat = self.get_object()
        chat_unread_marker = ChatUnreadMarker(chat)
        chat = chat_unread_marker()
        return self.response(chat, 200)

    @action(
        detail=True,
        methods=['GET'],
        url_path='messages',
        permission_classes=[IsMyChat],
        serializer_class=MessageSerializer,
    )
    def messages(self, request, pk=None):
        chat = self.get_object()
        message_retriever = AllChatMessagesRetriever(chat=chat)
        messages = message_retriever()
        return self.paginated_serialized_response(messages)

    def perform_create(self, serializer):
        chat_creator = ChatCreator(
            me=self.request.user,
            **serializer.validated_data,
        )
        return chat_creator()
