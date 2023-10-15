from django.contrib import admin
from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ['image',]


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['title',]
    list_display = ['id', 'title', ]
    inlines = [ImageInline,]

admin.site.register(Image)
