from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=100, unique=True)
    short_description = models.TextField('Короткое описание', blank=True)
    long_description = HTMLField('Полное описание', blank=True)
    lat = models.DecimalField('Широта', max_digits=17, decimal_places=14)
    lon = models.DecimalField('Долгота', max_digits=17, decimal_places=14)

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_coordinates(self):
        return [self.lon, self.lat]


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        verbose_name='Место',
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField('Изображение', blank=False)
    image_num = models.PositiveIntegerField(
        'Номер изображения',
        db_index=True
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['place', 'image_num']

    def __str__(self):
        return f'{self.place.id}.{self.image_num}. {self.image.name}'
