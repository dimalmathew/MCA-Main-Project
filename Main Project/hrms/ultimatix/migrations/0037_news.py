# Generated by Django 2.1.5 on 2019-05-12 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatix', '0036_wage'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('head', models.CharField(blank=True, max_length=150, null=True)),
                ('desc', models.TextField()),
                ('img', models.ImageField(default='img/news/abc.png', upload_to='img/news/')),
            ],
        ),
    ]