# Generated by Django 5.0.4 on 2024-05-07 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='country',
            new_name='position',
        ),
    ]