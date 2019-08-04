# Generated by Django 2.0.13 on 2019-07-01 11:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson1', '0012_remove_company_company_abbr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='company_country',
        ),
        migrations.AlterField(
            model_name='company',
            name='company_address',
            field=models.TextField(blank=True, verbose_name='Corporate address'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_PO',
            field=models.CharField(max_length=50, verbose_name="Client's reference"),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson1.Company', verbose_name='Client'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_ref',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='My reference'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_startdate',
            field=models.DateField(default=datetime.date.today, verbose_name='Start date'),
        ),
    ]