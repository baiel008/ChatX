from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='user_list')
router.register(r'anonymous', AnonymousChatViewSet, basename='anonymous_list')
router.register(r'participant', AnonymousChatParticipantViewSet, basename='participant_list')
router.register(r'message', MessageViewSet, basename='message_list')
router.register(r'deleted', DeletedMessageLogViewSet, basename='deleted_list')
router.register(r'entry', EntryLogViewSet, basename='entry_list')
# router.register(r'notification', NotificationViewSet, basename='notification_list')


urlpatterns = [
    path('', include(router.urls)),

]