# Generated by Django 2.0.7 on 2018-07-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20180722_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='website',
            field=models.URLField(default='https://www.mmust.ac.ke'),
        ),
    ]
