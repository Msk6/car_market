# Generated by Django 2.2.13 on 2020-09-06 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_car_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car_image',
            new_name='img',
        ),
    ]