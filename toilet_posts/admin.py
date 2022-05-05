from django.contrib import admin
from .models import Author, Toilet, ToiletGallery


@admin.register(Toilet)
class ToiletAdmin(admin.ModelAdmin):
    list_display = ["author", "user_tg_id", "rating", "confirmed", "id"]
    list_filter = ["author", "confirmed"]


admin.site.register(Author)

admin.site.register(ToiletGallery)
