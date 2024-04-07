from django.contrib import admin

# Register your models here.
from app.models import Book

class bookAdmim(admin.ModelAdmin):
    list_display =['name','author']
    search_fields =['author']

admin.site.register(Book,bookAdmim)