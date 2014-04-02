from django.contrib import admin
from models import Contact

class AdminContact(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_email', 'telephone_number', 'message', 'post_date')
    readonly_fields = ('contact_name', 'contact_email', 'telephone_number', 'message', 'post_date')

admin.site.register(Contact, AdminContact)