from django.contrib import admin

from .models import Category, Location, Post

# Я не понял для чего это нужно ~_~


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'location', 'category']
    search_fields = ['title', 'text']
    list_filter = ['pub_date', 'location', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


class LocationAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
