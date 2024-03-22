# Generated by Django 4.2.3 on 2024-03-22 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediverse', '0005_alter_chathistory_chatbot_response'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chathistory',
            name='chatbot_response',
        ),
        migrations.AddField(
            model_name='chathistory',
            name='chatbot_response_list',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='chathistory',
            name='chatbot_response_str',
            field=models.CharField(default='', max_length=255),
        ),
    ]