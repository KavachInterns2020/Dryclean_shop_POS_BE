# Generated by Django 3.0.7 on 2020-08-21 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200820_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_amount',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='total_amount',
        ),
    ]
