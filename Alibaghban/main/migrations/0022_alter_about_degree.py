# Generated by Django 4.2 on 2023-07-22 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_about_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='degree',
            field=models.CharField(choices=[('PhD', 'PhD'), ('Master', 'Master'), ("Bachelor's", "Bachelor's")], max_length=50),
        ),
    ]
