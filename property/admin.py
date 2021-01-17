from django.contrib import admin

# Register your models here.
from property.models import Property


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'ownerName', 'sold')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'ownerName')
    list_editable = ('sold', 'price')
    list_filter = ('sold', 'ownerName')

admin.site.register(Property, PropertyAdmin)