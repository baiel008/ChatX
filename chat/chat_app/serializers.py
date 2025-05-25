from rest_framework import serializers
from .models import *



class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['last_name', 'first_name']


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