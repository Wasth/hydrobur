# Generated by Django 2.0.4 on 2018-04-23 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_nasos_coef'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turbobur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('davl', models.FloatField()),
                ('d', models.FloatField()),
            ],
        ),
    ]
