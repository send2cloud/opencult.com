# Generated by Django 2.0.1 on 2018-01-30 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20180130_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.CharField(default='default address', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='maps_url',
            field=models.URLField(default='http://maps.com'),
            preserve_default=False,
        ),
    ]
