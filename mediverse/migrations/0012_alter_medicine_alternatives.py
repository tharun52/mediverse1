# Generated by Django 4.2.3 on 2024-03-22 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediverse', '0011_rename_alternative_medicine_alternatives'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='alternatives',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]