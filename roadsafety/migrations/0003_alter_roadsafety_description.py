# Generated by Django 4.1.4 on 2023-03-20 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadsafety', '0002_alter_roadsafety_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roadsafety',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
