# Generated by Django 3.1.7 on 2021-10-26 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0019_placedorders_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='placedorders',
            name='images',
            field=models.CharField(default='', max_length=3000),
            preserve_default=False,
        ),
    ]