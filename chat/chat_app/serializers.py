from rest_framework import serializers
from .models import *



class UserListProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'status']


class UserDetailProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'status', 'is_staff', 'is_active',
                  'last_seen', 'groups']



class UserProfileListSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class AnonymousChatSerializers(serializers.ModelSerializer):
    class Meta:
        model = AnonymousChat
        fields = '__all__'


class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class DeletedMessageLogSerializers(serializers.ModelSerializer):
    class Meta:
        model = DeletedMessageLog
        fields = '__all__'


class EntryLogSerializers(serializers.ModelSerializer):
    class Meta:
        model = EntryLog
        fields = '__all__'


class NotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class GroupChatSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'