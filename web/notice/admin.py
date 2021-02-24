from django.contrib import admin
from .models import *

# Register your models here.
class NoticeAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'writer', 
        'hits',
        'pub_date',
        )
    search_fields = ('title', 'content')
    
admin.site.register(Post)
