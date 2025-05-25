from django.contrib import admin
from django.contrib.admin import TabularInline
from .models import *


admin.site.register(UserProfile)
admin.site.register(AnonymousChat)
admin.site.register(Message)
admin.site.register(DeletedMessageLog)
admin.site.register(EntryLog)
admin.site.register(Notification)
admin.site.register(GroupChat)
