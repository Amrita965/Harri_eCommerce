# Generated by Django 5.0 on 2025-01-08 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SignUp', '0006_userinfo_password_reset_code_alter_userinfo_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='reset_code_created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password_reset_code',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
