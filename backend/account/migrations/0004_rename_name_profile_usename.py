# Generated by Django 4.2 on 2023-04-24 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='usename',
        ),
    ]
