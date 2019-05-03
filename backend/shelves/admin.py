from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    fieldsets = (
        ('ID',      {'fields': ('id',)}),
        ('タイトル',      {'fields': ('title',)}),
        ('画像URL',      {'fields': ('cover_url',)}),
    )

admin.site.register(Book, BookAdmin)

