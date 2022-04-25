from chats.models import Chat
from djangochat.services import BaseService


class ChatArchiver(BaseService):
    def __init__(self, chat: Chat):
        self.chat = chat

    def act(self):
        return self.archive_chat(self.chat)

    def archive_chat(self, chat: Chat):
        chat.is_archived = True
        chat.save()
        return chat
