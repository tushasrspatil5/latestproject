# Generated by Django 3.1.7 on 2021-11-11 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0046_orders_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_accept_time',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
