from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'user', UserProfile, basename='user_list')
router.register(r'anonymous', AnonymousChat, basename='anonymous_list')
router.register(r'participant', AnonymousChatParticipant, basename='participant_list')
router.register(r'message', Message, basename='message_list')
router.register(r'deleted', DeletedMessageLog, basename='deleted_list')
router.register(r'entry', EntryLog, basename='entry_list')
router.register(r'notification', Notification, basename='notification_list')


urlpatterns = [
    path('', include(router.urls)),

]