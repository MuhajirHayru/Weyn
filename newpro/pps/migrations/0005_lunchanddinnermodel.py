# Generated by Django 5.1.7 on 2025-03-06 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pps', '0004_rename_drink_drinkmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='lunchanddinnermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lunchanddinnerfoto', models.ImageField(upload_to='lunchanddinnerfoto')),
            ],
        ),
    ]
