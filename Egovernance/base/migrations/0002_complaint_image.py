# Generated by Django 5.0.6 on 2024-05-24 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/'),
        ),
    ]