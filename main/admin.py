from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Attendance, Comment, Cult, Event, Membership, Profile


# User
class OpCuAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_joined', 'last_login', 'id',)


admin.site.unregister(User)
admin.site.register(User, OpCuAdmin)


# Profile
admin.site.register(Profile)


# Cult
class CultAdmin(admin.ModelAdmin):
    list_display = ('name', 'city',)


admin.site.register(Cult, CultAdmin)


# Event
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'cult', 'date', 'time', 'venue',)


admin.site.register(Event, EventAdmin)


# Membership
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('cult', 'user', 'role', 'date_joined',)


admin.site.register(Membership, MembershipAdmin)


# Attendance
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'date_rsvped',)


admin.site.register(Attendance, AttendanceAdmin)


# Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ('date_posted', 'body', 'author', 'event',)


admin.site.register(Comment, CommentAdmin)
