from django.contrib import admin

from .models import Post,Tag

admin.site.register(Post)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('tag',)}
