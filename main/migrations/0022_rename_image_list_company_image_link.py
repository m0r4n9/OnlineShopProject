# Generated by Django 4.1.7 on 2023-04-23 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_company_image_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='image_list',
            new_name='image_link',
        ),
    ]
