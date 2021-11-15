from django.contrib import admin

from .models import CharacterCard

class CharacterCardAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)

admin.site.register(CharacterCard, CharacterCardAdmin)