# Generated by Django 4.1.3 on 2024-01-12 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='otp',
            new_name='generated_otp',
        ),
    ]
