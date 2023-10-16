from django.contrib import admin
from django.utils.html import format_html
from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ('image_tag',)
    fields = ['image', 'image_tag',]

    def image_tag(self, instance):
        return format_html('<img src="{}" style="max-height: 200px;" />', instance.image.url)

    image_tag.short_description = 'Превью'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['title',]
    list_display = ['title', 'id',]
    inlines = [ImageInline,]

admin.site.register(Image)
