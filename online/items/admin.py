from django.contrib import admin
from .models import Category, Item
# Register your models here.
# to tell admin to show database in admin interface only
admin.site.register(Category)
admin.site.register(Item)