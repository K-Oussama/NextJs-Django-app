from django.contrib import admin
from mptt.admin import MPTTModelAdmin
# Register your models here.

from .models import(
    Category,
    Post,
    PostImage,
)
admin.site.register(Category, MPTTModelAdmin)

class PostImageInline(admin.TabularInline):
    model = PostImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
       PostImageInline 
    ]