# Generated by Django 4.2.6 on 2023-11-01 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0015_alter_image_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_num',
            field=models.PositiveIntegerField(db_index=True, default='create_new_image_num', verbose_name='Номер изображения'),
        ),
    ]