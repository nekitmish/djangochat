from chats.models import Chat
from djangochat.services import BaseService
from messages.models import Message


class MessageCreator(BaseService):
    def __init__(self, sender, recipient, body: str):
        self.sender = sender
        self.recipient_id = recipient
        self.body = body

    def act(self):
        sender_chat_instance = self.get_sender_chat_instance(self.sender, self.recipient_id)
        recipient_chat_instance = self.get_recipient_chat_instance(self.sender, self.recipient_id)

        return self.create_message(
            sender=self.sender,
            recipient_id=self.recipient_id,
            sender_chat_instance=sender_chat_instance,
            recipient_chat_instance=recipient_chat_instance,
            body=self.body,
        )

    def get_sender_chat_instance(self, sender, recipient_id):
        return Chat.objects.get(me=sender, companion_id=recipient_id)

    def get_recipient_chat_instance(self, sender, recipient_id):
        return Chat.objects.get_or_create(me_id=recipient_id, companion=sender)

    def create_message(self, sender, recipient_id, sender_chat_instance, recipient_chat_instance, body):
        return Message.objects.create(
            sender=sender,
            recipient_id=recipient_id,
            sender_chat=sender_chat_instance,
            recipient_chat=recipient_chat_instance,
            body=body,
        )
