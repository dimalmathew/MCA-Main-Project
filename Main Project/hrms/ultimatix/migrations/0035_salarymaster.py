# Generated by Django 2.1.5 on 2019-05-11 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatix', '0034_auto_20190508_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salarymaster',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('bs', models.FloatField(blank=True, null=True)),
                ('con', models.FloatField(blank=True, null=True)),
                ('hra', models.FloatField(blank=True, null=True)),
                ('city', models.FloatField(blank=True, null=True)),
                ('sundry', models.FloatField(blank=True, null=True)),
                ('ptax', models.FloatField(blank=True, null=True)),
                ('pf', models.FloatField(blank=True, null=True)),
                ('esis', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
