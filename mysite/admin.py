# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from mysite.models import UserInfo, Contact, Tag, CheckImage, CheckImageRecord


class TagInline(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')  # list
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        # ['Advance', {
        #     'classes': ('collapse',),
        #     'fields': ('age',),
        # }]
    )


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_id')  # list
    fieldsets = (
        ['Main', {
            'fields': ('name', 'contact')
        }],
    )


# 注册 数据模型 到 admin ,然后可以通过后台 来管理数据
admin.site.register(Contact, ContactAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register([UserInfo, CheckImage, CheckImageRecord])
