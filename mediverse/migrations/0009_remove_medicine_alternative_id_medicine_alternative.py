# Generated by Django 4.2.3 on 2024-03-22 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediverse', '0008_remove_inventory_name_alter_inventory_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='alternative_id',
        ),
        migrations.AddField(
            model_name='medicine',
            name='alternative',
            field=models.CharField(default=None, max_length=255, null=True, blank=True),
            preserve_default=False,
        ),
    ]
