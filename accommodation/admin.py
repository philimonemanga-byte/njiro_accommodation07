from django.contrib import admin
from .models import Profile, Room, ContactMessage


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'user',
        'role',
        'phone'
    )

    list_filter = (
        'role',
    )

    search_fields = (
        'full_name',
        'user__username',
    )


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'owner',
        'room_type',
        'price',
        'location',
        'available'
    )

    list_filter = (
        'room_type',
        'available',
    )

    search_fields = (
        'title',
        'location',
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        'student',
        'room',
        'created_at'
    )

    search_fields = (
        'student__username',
    )
