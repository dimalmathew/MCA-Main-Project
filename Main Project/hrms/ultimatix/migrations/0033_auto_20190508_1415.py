# Generated by Django 2.1.5 on 2019-05-08 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatix', '0032_leave_ltype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='nof',
            field=models.FloatField(blank=True, null=True),
        ),
    ]