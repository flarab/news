from django.contrib import admin

# Register your models here.

from .models import New, Tag, Image


class ImageInline(admin.TabularInline):
    model = Image
    raw_id_fields = ('new',)


class NewAdmin(admin.ModelAdmin):
    list_display = [field.name for field in New._meta.fields]
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'body')
    inlines = [ImageInline]


admin.site.register(New, NewAdmin)
admin.site.register(Tag)
