# Generated by Django 4.2 on 2023-05-01 01:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marketplace', '0002_rename_product_products'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
