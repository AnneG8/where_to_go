# Generated by Django 4.2.6 on 2023-10-30 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_alter_image_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['place_id', 'image_num'], 'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
    ]
