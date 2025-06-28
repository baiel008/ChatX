from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'anonymous', AnonymousChatViewSet, basename='anonymous_list')
router.register(r'message', MessageViewSet, basename='message_list')
router.register(r'deleted', DeletedMessageLogViewSet, basename='deleted_list')
router.register(r'entry', EntryLogViewSet, basename='entry_list')
router.register(r'notification', NotificationViewSet, basename='notification_list')
router.register(r'group', GroupChatViewSet, basename='group_name')


urlpatterns = [
    path('', include(router.urls)),
    path('user/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
]