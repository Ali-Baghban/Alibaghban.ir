# Generated by Django 4.2 on 2023-07-21 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_resume_column'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='column',
            field=models.BooleanField(choices=[('Left', True), ('Right', False)], default=True),
        ),
    ]
