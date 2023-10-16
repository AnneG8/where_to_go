from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from places.models import Place, Image


class ImageInlineAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ['image_preview',]
    fields = ['image', 'image_preview', 'image_num',]

    def image_preview(self, instance):
        return format_html('<img src="{}" style="max-height: 200px;" />', instance.image.url)

    image_preview.short_description = 'Превью'


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    sortable = 'image_num'


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    search_fields = ['title',]
    list_display = ['title', 'id',]
    inlines = [ImageInlineAdmin,]
