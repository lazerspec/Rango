from django.contrib import admin
from rango.models import Category, Page

#admin.site.register(Category)
#admin.site.register(Page, PageAdmin)

# Register your models here.

#Create a page admin class that inherits from admin.ModelAdmin

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)