# Generated by Django 5.0 on 2023-12-28 23:35

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STORE', '0013_cart_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='uuid_id',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='uuid_id',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
    ]