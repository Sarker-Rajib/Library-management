from django.contrib import admin

# Register your models here.
from .models import BookCategory, Book, Review

# Register your models here.
class BrandSlug(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    list_display = ['name', 'slug']

admin.site.register(BookCategory, BrandSlug)
admin.site.register(Book)
admin.site.register(Review)