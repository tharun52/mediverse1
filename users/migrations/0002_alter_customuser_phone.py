# Generated by Django 4.2.3 on 2024-03-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.PositiveIntegerField(),
        ),
    ]
