from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'photo')
    # search_fields = ('uuid')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    # search_fields = ('name')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'name', 'deadline', 'status', 'priority', 'created_at', 'updated_at')
    # search_fields = ('category', 'name', 'status', 'priority')
    list_filter = ('status', 'deadline')

