# Generated by Django 4.2 on 2023-07-22 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0020_alter_message_sent_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sent_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 22, 15, 17, 6, 881326)),
        ),
    ]
