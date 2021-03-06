# Generated by Django 3.1.7 on 2021-10-23 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0017_auto_20211023_0648'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacedOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customername', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('items', models.CharField(max_length=2000)),
                ('address', models.CharField(max_length=2000)),
                ('state', models.CharField(max_length=2000)),
                ('pincode', models.CharField(max_length=2000)),
                ('phone', models.CharField(max_length=2000)),
                ('price', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
