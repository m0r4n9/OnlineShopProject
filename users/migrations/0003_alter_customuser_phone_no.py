# Generated by Django 4.1.7 on 2023-04-13 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_no',
            field=models.CharField(max_length=10),
        ),
    ]