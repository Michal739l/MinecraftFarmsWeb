# Generated by Django 5.1.1 on 2024-11-16 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farms', '0005_farm_description_farm_difficulty_farm_efficiency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='farm_images/'),
        ),
    ]
