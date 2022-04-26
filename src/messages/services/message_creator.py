from chats.models import Chat
from djangochat.services import BaseService
from messages.models import Message


class MessageCreator(BaseService):
    def __init__(self, sender, recipient, body: str):
        self.sender = sender
        self.recipient = recipient
        self.body = body

    def act(self):
        sender_chat_instance = self.get_sender_chat_instance(self.sender, self.recipient)
        recipient_chat_instance = self.get_recipient_chat_instance(self.sender, self.recipient)

        return self.create_message(
            sender=self.sender,
            recipient=self.recipient,
            sender_chat_instance=sender_chat_instance,
            recipient_chat_instance=recipient_chat_instance,
            body=self.body,
        )

    def get_sender_chat_instance(self, sender, recipient):
        return Chat.objects.get(me=sender, companion=recipient)

    def get_recipient_chat_instance(self, sender, recipient):
        chat, _ = Chat.objects.get_or_create(me=recipient, companion=sender)
        return chat

    def create_message(self, sender, recipient, sender_chat_instance, recipient_chat_instance, body):
        return Message.objects.create(
            sender=sender,
            recipient=recipient,
            sender_chat=sender_chat_instance,
            recipient_chat=recipient_chat_instance,
            body=body,
        )
