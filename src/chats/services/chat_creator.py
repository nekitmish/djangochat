from chats.models import Chat
from djangochat.services import BaseService
from users.models import User


class ChatCreator(BaseService):

    def __init__(self, me: User, companion):
        self.me = me
        self.companion = companion

    def act(self):
        return self.create_my_chat()

    def create_my_chat(self):
        return Chat.objects.create(
            me=self.me,
            companion_id=self.companion,
        )
