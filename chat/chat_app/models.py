from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
import uuid

STATUS_CHOICES = (
    ('simple', 'Simple'),
    ('pro', 'Pro'),
)

class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(16), MaxValueValidator(65)],
        null=True,
        blank=True
    )

    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='simple')
    last_seen = models.DateTimeField(null=True, blank=True)
    is_invisible = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class AnonymousChat(models.Model):
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='created_anon_chats')
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    max_participants = models.PositiveIntegerField(default=2)
    password = models.CharField(max_length=128, null=True, blank=True)
    is_one_time = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def is_expired(self):
        return self.expires_at and timezone.now() > self.expires_at

    def __str__(self):
        return f'{self.creator}, Created'


class AnonymousChatParticipant(models.Model):
    chat = models.ForeignKey(AnonymousChat, on_delete=models.CASCADE, related_name='participants')
    user = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.SET_NULL)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Participant {self.user} in {self.chat}"


class Message(models.Model):
    chat = models.ForeignKey(AnonymousChat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Msg from {self.sender} or {self.chat}"


class DeletedMessageLog(models.Model):
    original_message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='deletion_log')
    deleted_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Deleted by {self.deleted_by} or Deleted {self.original_message}"


class EntryLog(models.Model):
    chat = models.ForeignKey(AnonymousChat, on_delete=models.CASCADE, related_name='entry_logs')
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} entered, {self.chat}"


class Notification(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notif to {self.user}: {self.message} "
