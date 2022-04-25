from rest_framework.permissions import BasePermission

from chats.models import Chat


class IsMyChat(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, chat: Chat):
        return chat.me_id == request.user.id
