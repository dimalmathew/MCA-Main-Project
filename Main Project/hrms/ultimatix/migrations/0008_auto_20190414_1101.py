# Generated by Django 2.1.5 on 2019-04-14 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatix', '0007_auto_20190414_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designation',
            name='d_max',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
