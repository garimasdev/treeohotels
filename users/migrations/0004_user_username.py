# Generated by Django 5.1.5 on 2025-02-21 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_phone_agentprofile_customerprofile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='default_username', max_length=150, unique=True),
        ),
    ]
