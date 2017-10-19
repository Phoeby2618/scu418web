# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from forum.models import UserProfile, Note, Comment

from django.contrib import admin

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    pass


class NoteAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Comment, CommentAdmin)