# Generated by Django 2.1.5 on 2019-05-01 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatix', '0029_timesheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='tdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='thours',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
