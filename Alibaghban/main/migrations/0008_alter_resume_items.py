# Generated by Django 4.2 on 2023-07-19 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_resume_item_remove_resume_column_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='items',
            field=models.ManyToManyField(blank=True, to='main.resume_item'),
        ),
    ]