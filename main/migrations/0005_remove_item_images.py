# Generated by Django 4.1.7 on 2023-03-13 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_item_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='images',
        ),
    ]
