# Generated by Django 2.0.13 on 2019-07-01 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson1', '0009_auto_20190701_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_address',
            field=models.TextField(default='Not specified'),
            preserve_default=False,
        ),
    ]
