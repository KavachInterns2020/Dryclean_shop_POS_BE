# Generated by Django 3.0.7 on 2020-09-12 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshop',
            name='user',
        ),
    ]
