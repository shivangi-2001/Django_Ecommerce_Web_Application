# Generated by Django 5.0 on 2023-12-27 21:10

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STORE', '0004_auto_20231227_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='uuid_id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
