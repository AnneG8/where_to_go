# Generated by Django 4.2.6 on 2023-11-01 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_alter_image_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-place', 'image_num'], 'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
    ]
