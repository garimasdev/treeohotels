# Generated by Django 5.1.5 on 2025-02-18 09:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TourPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('destination', models.CharField(max_length=255)),
                ('duration', models.PositiveIntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour_packages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TourInclusionsExclusions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inclusions', models.TextField(help_text='Things included in the package')),
                ('exclusions', models.TextField(help_text='Things not included in the package')),
                ('tour', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inclusions_exclusions', to='tours.tourpackage')),
            ],
        ),
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tour_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='tours.tourpackage')),
            ],
        ),
        migrations.CreateModel(
            name='TourPackageReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])),
                ('review_text', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour_reviews', to=settings.AUTH_USER_MODEL)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='tours.tourpackage')),
            ],
        ),
        migrations.CreateModel(
            name='TourPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancellation_policy', models.TextField()),
                ('refund_policy', models.TextField()),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('tour', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='policies', to='tours.tourpackage')),
            ],
        ),
        migrations.CreateModel(
            name='TourPricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gst_percentage', models.DecimalField(decimal_places=2, default=5.0, max_digits=5)),
                ('discount_percentage', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('extra_charges', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('tour', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pricing', to='tours.tourpackage')),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_number', models.PositiveIntegerField()),
                ('details', models.TextField()),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itineraries', to='tours.tourpackage')),
            ],
            options={
                'unique_together': {('tour', 'day_number')},
            },
        ),
    ]
