# Generated by Django 4.2 on 2023-07-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_profile_is_chosen'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='geo_location',
            field=models.CharField(default='32.7177373,51.5233033', max_length=150),
        ),
    ]
