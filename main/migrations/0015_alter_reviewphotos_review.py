# Generated by Django 4.1.7 on 2023-04-17 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_review_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewphotos',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='main.review'),
        ),
    ]
