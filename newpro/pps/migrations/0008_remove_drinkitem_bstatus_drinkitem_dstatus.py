# Generated by Django 5.1.6 on 2025-03-07 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pps', '0007_drinkitem_fooditem_order_delete_breakfastmodel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drinkitem',
            name='Bstatus',
        ),
        migrations.AddField(
            model_name='drinkitem',
            name='Dstatus',
            field=models.CharField(choices=[('juice', 'juice'), ('hot_drink', 'hot_drink'), ('soft_drinks', 'soft_drinks')], default='juice', max_length=100),
        ),
    ]
