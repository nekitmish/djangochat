from chats.models import Chat
from djangochat.services import BaseService


class AllChatMessagesRetriever(BaseService):
    def __init__(self, chat: Chat):
        self.chat = chat

    def act(self):
        sent_messages = self.chat.sent_messages.all()
        received_messages = self.chat.received_messages.all()

        return sent_messages.union(received_messages).order_by('-created_at')
