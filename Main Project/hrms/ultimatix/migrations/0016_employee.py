# Generated by Django 2.1.5 on 2019-04-19 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatix', '0015_delete_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('e_id', models.AutoField(default='1022891', primary_key=True, serialize=False)),
                ('e_fname', models.CharField(max_length=50)),
                ('e_lname', models.CharField(max_length=50)),
                ('e_sname', models.CharField(max_length=50)),
                ('e_dob', models.DateField()),
                ('e_bgroup', models.CharField(max_length=3)),
                ('e_mstatus', models.CharField(max_length=1)),
                ('e_nationality', models.CharField(max_length=50)),
                ('e_disb', models.CharField(max_length=1)),
                ('e_gender', models.CharField(max_length=1)),
                ('e_paddr1', models.CharField(max_length=50)),
                ('e_paddr2', models.CharField(max_length=50)),
                ('e_paddr3', models.CharField(max_length=50)),
                ('e_caddr1', models.CharField(max_length=50)),
                ('e_caddr2', models.CharField(max_length=50)),
                ('e_caddr3', models.CharField(max_length=50)),
                ('e_email', models.CharField(max_length=100)),
                ('e_mnumber', models.IntegerField()),
                ('e_doj', models.DateField()),
                ('e_qfn', models.CharField(max_length=50)),
                ('e_prev_exp', models.IntegerField()),
                ('e_prev_cmp', models.CharField(max_length=50)),
                ('e_cl', models.IntegerField(default=0)),
                ('e_sl', models.IntegerField(default=0)),
                ('e_el', models.IntegerField(default=0)),
                ('e_fl', models.IntegerField(default=0)),
                ('e_status', models.CharField(max_length=1)),
                ('e_pwd', models.CharField(max_length=100)),
            ],
        ),
    ]