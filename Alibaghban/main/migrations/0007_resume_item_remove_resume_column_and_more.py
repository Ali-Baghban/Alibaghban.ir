# Generated by Django 4.2 on 2023-07-19 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_skill_1_level_skill_skill_level_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(blank=True, null=True)),
                ('year', models.CharField(blank=True, max_length=50)),
                ('institution', models.CharField(blank=True, max_length=150)),
                ('break_point', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='resume',
            name='column',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='institution',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='sub_title',
        ),
        migrations.AddField(
            model_name='resume',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, to='main.resume_item'),
        ),
    ]
