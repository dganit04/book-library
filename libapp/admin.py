from django.contrib import admin

from .models import Item

class ItemAdmin(admin.ModelAdmin):
# 	Display data instead of 'item object'
	list_display = ['title', 'author', 'description', 'pic']

admin.site.register(Item, ItemAdmin)