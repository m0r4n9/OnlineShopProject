# Generated by Django 4.1.7 on 2023-04-14 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_remove_favoritelist_products_favoritelist_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritelist',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
