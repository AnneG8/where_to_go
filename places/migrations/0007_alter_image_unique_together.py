# Generated by Django 4.2.6 on 2023-10-30 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_image_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='image',
            unique_together=set(),
        ),
    ]