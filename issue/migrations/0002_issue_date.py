# Generated by Django 4.1.4 on 2023-03-21 03:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
