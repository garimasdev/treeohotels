# Generated by Django 5.1.5 on 2025-03-03 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourpackage',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
