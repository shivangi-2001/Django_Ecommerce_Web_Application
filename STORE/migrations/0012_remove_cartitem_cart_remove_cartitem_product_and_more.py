# Generated by Django 5.0 on 2023-12-28 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('STORE', '0011_auto_20231228_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
