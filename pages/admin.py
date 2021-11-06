from django.contrib import admin
from .models import Team
from django.utils.html import format_html


# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src = "{}" width = "40" style="border-radius: 20px;"/>'.format(object.photo.url))

    thumbnail.short_description = "Image"

    list_display = ('id','thumbnail','first_name','last_name','designation','created_date')
    list_display_links = ('first_name','id')
    search_fields = ('id','first_name','designation')
    list_filter = ('designation',)

admin.site.register(Team, TeamAdmin)