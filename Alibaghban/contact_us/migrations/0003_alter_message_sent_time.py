# Generated by Django 4.2 on 2023-07-19 10:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0002_alter_message_sent_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sent_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 19, 13, 55, 1, 728020)),
        ),
    ]