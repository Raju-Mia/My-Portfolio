from django.contrib import admin

# Register your models here.

from .models import (
    AboutMe,
)

@admin.register(AboutMe)
class AboutMeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'fullname', 'nickname', 'profile', 'specialist', 'age', 'number', 'education', 'mail', 'linkedin', 'twitter', 'github', 'facebook', 'whatsapp', 'telegram', 'address', 'aboutme']

