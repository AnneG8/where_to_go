from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=100)
    description_short = models.CharField('Короткое описание',
                                         max_length=300,
                                         null=True,
                                         blank=True)
    description_long = models.TextField('Полное описание',
                                        null=True,
                                        blank=True)
    lat = models.DecimalField('Широта', max_digits=17, decimal_places=14)
    lon = models.DecimalField('Долгота', max_digits=17, decimal_places=14)

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title

    def get_coordinates(self):
        return (self.lon, self.lat)


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        verbose_name='Место',
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(verbose_name='Изображение', blank=False)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
