# Generated by Django 4.1.7 on 2023-03-21 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_gender_alter_customuser_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.BooleanField(default=False),
        ),
    ]
