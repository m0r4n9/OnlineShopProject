# Generated by Django 4.1.7 on 2023-04-17 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_productphotos_product_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productphotos',
            name='product_parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product'),
        ),
    ]
