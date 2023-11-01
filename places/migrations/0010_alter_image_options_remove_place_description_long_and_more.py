# Generated by Django 4.2.6 on 2023-11-01 19:29

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_alter_image_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-place__id', 'image_num'], 'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Полное описание'),
        ),
        migrations.RenameField(
            model_name='place',
            old_name='description_long',
            new_name='long_description',
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, verbose_name='Короткое описание'),
        ),
        migrations.RenameField(
            model_name='place',
            old_name='description_short',
            new_name='short_description',
        ),
        migrations.AlterField(
            model_name='image',
            name='image_num',
            field=models.PositiveIntegerField(db_index=True, verbose_name='Номер изображения'),
        ),
    ]
