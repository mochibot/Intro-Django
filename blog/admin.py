from django.contrib import admin

from .models import Blog, PersonalBlog

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'last_modified')

# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(PersonalBlog, BlogAdmin)