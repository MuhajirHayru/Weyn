# Generated by Django 5.1.6 on 2025-03-08 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pps', '0009_alter_fooditem_quntity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='need_time',
            field=models.TimeField(auto_created=True, blank=True, null=True),
        ),
    ]
