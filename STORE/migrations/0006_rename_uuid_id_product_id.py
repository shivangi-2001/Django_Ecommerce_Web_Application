# Generated by Django 5.0 on 2023-12-27 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('STORE', '0005_remove_product_id_alter_product_uuid_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='uuid_id',
            new_name='id',
        ),
    ]
