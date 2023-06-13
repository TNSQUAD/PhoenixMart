# Generated by Django 4.2.1 on 2023-06-13 13:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0016_alter_cartorder_sku"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartorder",
            name="price",
            field=models.DecimalField(decimal_places=2, default="1.99", max_digits=15),
        ),
        migrations.AlterField(
            model_name="cartorderproducts",
            name="price",
            field=models.DecimalField(decimal_places=2, default="1.99", max_digits=15),
        ),
        migrations.AlterField(
            model_name="cartorderproducts",
            name="total",
            field=models.DecimalField(decimal_places=2, default="1.99", max_digits=15),
        ),
        migrations.AlterField(
            model_name="product",
            name="old_price",
            field=models.DecimalField(decimal_places=2, default="2.99", max_digits=15),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, default="1.99", max_digits=15),
        ),
    ]
