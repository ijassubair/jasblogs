from django.contrib import admin
from pages.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_filter = ['article_ready']


admin.site.register(Contact, ContactAdmin)
