# Generated by Django 2.2.3 on 2019-08-03 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voizdata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logindata',
            name='user',
        ),
    ]