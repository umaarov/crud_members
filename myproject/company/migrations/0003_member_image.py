# Generated by Django 5.0.4 on 2024-05-07 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_rename_country_member_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.ImageField(default='images/about.jpg', upload_to='images/'),
        ),
    ]
