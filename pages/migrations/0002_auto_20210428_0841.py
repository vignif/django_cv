# Generated by Django 3.1.4 on 2021-04-28 08:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('date_founding', models.DateField(default=datetime.date.today, verbose_name='founding date')),
                ('url', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('date_founding', models.DateField(default=datetime.date.today, verbose_name='founding date')),
                ('url', models.CharField(max_length=18)),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='bd_date',
            field=models.DateField(default=datetime.date.today, verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='date_end',
            field=models.DateField(default=datetime.date.today, verbose_name='Finel date of employment'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='date_start',
            field=models.DateField(default=datetime.date.today, verbose_name='Initial date of employment'),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.userinfo')),
            ],
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.employer'),
        ),
    ]