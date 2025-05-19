from rest_framework import serializers
from .models import *



class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class AnonymousChatSerializers(serializers.ModelSerializer):
    class Meta:
        model = AnonymousChat
        fields = '__all__'


class AnonymousChatParticipantSerializers(serializers.ModelSerializer):
    class Meta:
        model = AnonymousChatParticipant
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
        field = '__all__'


class NotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'