# Generated by Django 4.0.1 on 2022-03-15 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0003_rename_image_profile_banner_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='interestList',
        ),
    ]
