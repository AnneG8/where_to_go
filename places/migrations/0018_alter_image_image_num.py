# Generated by Django 4.2.6 on 2023-11-05 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0017_alter_image_image_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_num',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Номер изображения'),
        ),
    ]
