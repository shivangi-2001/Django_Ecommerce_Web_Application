# Generated by Django 5.0 on 2023-12-28 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('STORE', '0007_cart_cartitem_cart_products'),
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
