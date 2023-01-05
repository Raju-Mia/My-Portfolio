from django.contrib import admin

# Register your models here.

from .models import (
    AboutMe,
    ContactForm
)

@admin.register(AboutMe)
class AboutMeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'fullname', 'nickname', 'profile', 'specialist', 'age', 'number', 'education', 'mail', 'linkedin', 'twitter', 'github', 'facebook', 'whatsapp', 'telegram', 'address', 'aboutme']


@admin.register(ContactForm)
class ContactFormModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'email_add', 'subject_name', 'message']


