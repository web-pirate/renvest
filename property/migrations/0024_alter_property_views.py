# Generated by Django 4.1.4 on 2023-03-03 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0023_remove_property_views_property_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='views',
            field=models.TextField(default=None, null=True),
        ),
    ]
