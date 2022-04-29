from django.contrib import admin
from .models import Author, Toilet


@admin.register(Toilet)
class ToiletAdmin(admin.ModelAdmin):
    list_display = ["author", "user_tg_id", "rating", "confirmed"]
    list_filter = ["author"]


admin.site.register(Author)

