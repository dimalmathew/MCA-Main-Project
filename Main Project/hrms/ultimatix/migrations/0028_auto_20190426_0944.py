# Generated by Django 2.1.5 on 2019-04-26 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatix', '0027_auto_20190424_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_members',
            fields=[
                ('pmid', models.AutoField(primary_key=True, serialize=False)),
                ('pmsdate', models.DateTimeField(blank=True, null=True)),
                ('pmedate', models.DateTimeField(blank=True, null=True)),
                ('pmstatus', models.CharField(max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_prev_exp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project_members',
            name='eid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ultimatix.Employee'),
        ),
        migrations.AddField(
            model_name='project_members',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ultimatix.Project'),
        ),
        migrations.AddField(
            model_name='project_members',
            name='rid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ultimatix.Project_roles'),
        ),
    ]
