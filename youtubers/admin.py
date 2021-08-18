from django.contrib import admin
from .models import Youtubers
from django.utils.html import format_html


class YtAdmin(admin.ModelAdmin):
    def myPhoto(self, object):
        return format_html('<img width="40" src="{}">'.format(object.photo.url))
    list_display = ('id', 'name', 'myPhoto', 'subs_count', 'is_featured')
    search_fields = ('name', 'camera_type')
    list_filter = ('city', 'camera_type')
    list_display_links = ('id', 'name',)
    list_editable = ('is_featured',)


# Register your models here.
admin.site.register(Youtubers, YtAdmin)
