# Generated by Django 4.1.3 on 2022-12-23 13:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_bascet'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bascet',
            new_name='Basket',
        ),
    ]
