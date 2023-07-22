# Generated by Django 4.2 on 2023-07-22 08:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0014_alter_message_sent_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='checked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='sent_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 22, 11, 37, 43, 844642)),
        ),
    ]
