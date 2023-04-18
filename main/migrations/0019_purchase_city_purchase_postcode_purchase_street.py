# Generated by Django 4.1.7 on 2023-04-17 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_purchase_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='city',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='purchase',
            name='postcode',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='purchase',
            name='street',
            field=models.CharField(default=None, max_length=100),
        ),
    ]