# Generated by Django 2.1.5 on 2019-04-24 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatix', '0026_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='pedate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
