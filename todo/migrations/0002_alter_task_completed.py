# Generated by Django 5.0.3 on 2024-11-14 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Completed',
            field=models.BooleanField(default=False),
        ),
    ]
