# Generated by Django 2.1.5 on 2019-04-14 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatix', '0006_designation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designation',
            name='d_max',
            field=models.IntegerField(blank=True),
        ),
    ]
