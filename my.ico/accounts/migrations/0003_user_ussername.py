# Generated by Django 5.0 on 2024-01-01 08:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_bio_user_date_of_birth_user_is_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ussername',
            field=models.CharField(default=datetime.datetime(2024, 1, 1, 8, 59, 13, 549504, tzinfo=datetime.timezone.utc), max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
