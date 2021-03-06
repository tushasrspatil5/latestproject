# Generated by Django 3.1.7 on 2021-10-12 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0014_prescription_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=500)),
                ('img_url1', models.CharField(max_length=500)),
                ('img_url2', models.CharField(max_length=500)),
                ('img_url3', models.CharField(max_length=500)),
                ('img_url4', models.CharField(max_length=500)),
                ('long_desc1', models.CharField(max_length=500)),
                ('long_desc2', models.CharField(max_length=500)),
                ('long_desc3', models.CharField(max_length=500)),
                ('long_desc4', models.CharField(max_length=500)),
                ('long_desc5', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('price_old', models.IntegerField()),
                ('percent_off', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=50)),
                ('sub_category', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
