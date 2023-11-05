from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin

from places.models import Place, Image


class ImageInlineAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ['show_image_preview',]
    fields = ['image', 'show_image_preview', 'image_num',]

    def show_image_preview(self, instance):
        return format_html('<img src="{}" style="max-height: 200px;" />', instance.image.url)

    show_image_preview.short_description = 'Превью'


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    sortable = 'image_num'
    ordering = ['-place_id', 'image_num']
    list_display = ('__str__', 'show_image_preview',)
    autocomplete_fields = ['place']

    def get_list_display_links(self, request, list_display):
        return ()

    def show_image_preview(self, instance):
        return format_html('<img src="{}" style="max-height: 200px;" />', instance.image.url)

    show_image_preview.short_description = 'Превью'


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    search_fields = ['title',]
    list_display = ['title', 'id',]
    inlines = [ImageInlineAdmin,]
