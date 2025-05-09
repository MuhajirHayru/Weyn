# Generated by Django 5.1.6 on 2025-03-07 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pps', '0006_breakfastmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='drinkitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('Bstatus', models.CharField(choices=[('juice', 'juice'), ('hot_drink', 'hot_drink'), ('soft_drinks', 'soft_drinks')], default='breakfast', max_length=100)),
                ('price', models.DecimalField(decimal_places=3, max_digits=12)),
                ('quntity', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fooditem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('Fstatus', models.CharField(choices=[('breakfast', 'breakfast'), ('lunch_and_dinner', 'lunch')], default='breakfast', max_length=100)),
                ('price', models.DecimalField(decimal_places=3, max_digits=12)),
                ('quntity', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('need_time', models.TimeField(auto_created=True)),
                ('custemer_name', models.CharField(max_length=100)),
                ('pohone_No', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('delivered', 'delivered')], default='pending', max_length=20)),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
                ('drink_items', models.ManyToManyField(blank=True, to='pps.drinkitem')),
                ('food_items', models.ManyToManyField(blank=True, to='pps.fooditem')),
            ],
        ),
        migrations.DeleteModel(
            name='breakfastmodel',
        ),
        migrations.DeleteModel(
            name='drinkmodel',
        ),
        migrations.DeleteModel(
            name='foodlists',
        ),
        migrations.DeleteModel(
            name='lunchanddinnermodel',
        ),
    ]
