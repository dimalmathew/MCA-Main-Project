# Generated by Django 2.1.5 on 2019-04-13 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatix', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designation',
            name='d_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
