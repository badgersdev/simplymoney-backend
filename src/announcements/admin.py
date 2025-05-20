from django.contrib import admin
from .models import Announcement, AnnouncementImage


class AnnouncementImageInline(admin.TabularInline):
    model = AnnouncementImage
    extra = 0  # nie dodawaj pustych pól
    readonly_fields = ["preview"]

    def preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="150" />'
        return "Brak zdjęcia"

    preview.allow_tags = True
    preview.short_description = "Podgląd zdjęcia"


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("label", "category", "seller_type",
                    "exchange_type", "timestamp")
    search_fields = ("label", "description", "email", "phone")
    list_filter = ("category", "seller_type", "exchange_type", "timestamp")
    inlines = [AnnouncementImageInline]
