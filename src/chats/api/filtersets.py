from django_filters import rest_framework as filters

from chats.models import Chat


class ChatFilter(filters.FilterSet):
    class Meta:
        model = Chat
        fields = ['is_archived', 'is_unread']
