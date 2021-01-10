from django.contrib import admin
from .models import Category, Advertisement, Review, Location

# Register your models here.

admin.site.register(Category)
admin.site.register(Advertisement)
admin.site.register(Review)
admin.site.register(Location)