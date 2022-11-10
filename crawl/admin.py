from django.contrib import admin
from crawl.models import Post,Page


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'symbol', 'company_name',
                    'create_at', 'publish_date','url','update_at')

# Register your models here.


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('post', 'html',
                    'create_at', 'update_at')