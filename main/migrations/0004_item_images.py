# Generated by Django 4.1.7 on 2023-03-13 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='images',
            field=models.FileField(null=True, upload_to='images/'),
        ),
    ]
