# Generated by Django 4.1.5 on 2023-05-10 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timestamps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timestamps',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
