# Generated by Django 5.1.4 on 2025-01-10 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProductCategory', '0003_subcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='SubCategory_name',
            new_name='subcategory_name',
        ),
    ]
