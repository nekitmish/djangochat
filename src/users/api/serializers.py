from rest_framework import serializers

from users.models import User


class UserReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
        ]


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'bio',
        ]
