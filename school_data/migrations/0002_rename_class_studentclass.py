# Generated by Django 5.0.3 on 2024-03-11 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Class',
            new_name='StudentClass',
        ),
    ]