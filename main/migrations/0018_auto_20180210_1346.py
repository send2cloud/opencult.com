# Generated by Django 2.0.1 on 2018-02-10 13:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='order',
        ),
        migrations.AddField(
            model_name='comment',
            name='posted_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
