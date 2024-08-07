# Generated by Django 5.0.4 on 2024-05-08 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_alter_member_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_img', models.ImageField(default='about.jpg', upload_to='images/')),
                ('header', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
        ),
    ]
