# Generated by Django 2.1.5 on 2019-04-23 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatix', '0024_employee_employee_desig_employee_sal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='e_bgroup',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_cl',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_el',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_fl',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_gender',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_lname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_mnumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_mstatus',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_nationality',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_paddr1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_paddr2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_paddr3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_qfn',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_sl',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_sname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
