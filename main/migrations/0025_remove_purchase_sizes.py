# Generated by Django 4.1.7 on 2023-04-24 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_purchase_sizes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='sizes',
        ),
    ]
