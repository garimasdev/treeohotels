# Generated by Django 5.1.5 on 2025-02-21 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
