from chats.models import Chat
from djangochat.services import BaseService


class ChatUnreadMarker(BaseService):
    def __init__(self, chat: Chat):
        self.chat = chat

    def act(self):
        return self.mark_unread(self.chat)

    def mark_unread(self, chat: Chat):
        chat.is_unread = True
        chat.save()
        return chat
