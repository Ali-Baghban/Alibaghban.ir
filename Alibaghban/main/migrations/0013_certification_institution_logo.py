# Generated by Django 4.2 on 2023-07-22 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_resume_column'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification',
            name='institution_logo',
            field=models.ImageField(blank=True, upload_to='certs/%Y/%m/%d/'),
        ),
    ]
