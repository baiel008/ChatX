from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers


class AnonymousChatViewSet(viewsets.ModelViewSet):
    queryset = AnonymousChat.objects.all()


class AnonymousChatParticipantViewSet(viewsets.ModelViewSet):
    queryset = AnonymousChatParticipant.objects.all()
    serializer_class = AnonymousChatParticipantSerializers


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers


class DeletedMessageLogViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = DeletedMessageLogSerializers


class EntryLogViewSet(viewsets.ModelViewSet):
    queryset = EntryLog.objects.all()
    serializer_class = EntryLogSerializers


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializers

