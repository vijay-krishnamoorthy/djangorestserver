# Generated by Django 2.2.4 on 2019-08-13 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dongleform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=10)),
                ('pincode', models.CharField(max_length=6)),
            ],
            options={
                'verbose_name': 'Dongleform',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('femail', models.CharField(max_length=100)),
                ('fsubject', models.CharField(max_length=100)),
                ('fmessage', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Postform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=10)),
                ('pincode', models.CharField(max_length=6)),
            ],
            options={
                'verbose_name': 'Postform',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Preform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=10)),
                ('pincode', models.CharField(max_length=6)),
            ],
            options={
                'verbose_name': 'Preform',
                'ordering': ('name',),
            },
        ),
    ]