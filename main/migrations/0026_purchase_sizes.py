# Generated by Django 4.1.7 on 2023-04-24 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_remove_purchase_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='sizes',
            field=models.JSONField(default=None),
        ),
    ]