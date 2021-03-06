# Generated by Django 2.1.5 on 2019-05-07 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatix', '0030_auto_20190501_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False)),
                ('sdate', models.DateField(blank=True, null=True)),
                ('edate', models.DateField(blank=True, null=True)),
                ('nof', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=1, null=True)),
                ('desc', models.CharField(blank=True, max_length=150, null=True)),
                ('reqdate', models.DateField(blank=True, null=True)),
                ('remarks', models.CharField(blank=True, max_length=150, null=True)),
                ('queueid', models.CharField(blank=True, max_length=150, null=True)),
                ('updtby', models.CharField(blank=True, max_length=150, null=True)),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ultimatix.Employee')),
            ],
        ),
    ]
