# Generated by Django 4.1.7 on 2023-04-12 18:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_post_time_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 12, 18, 11, 49, 968502, tzinfo=datetime.timezone.utc)),
        ),
    ]