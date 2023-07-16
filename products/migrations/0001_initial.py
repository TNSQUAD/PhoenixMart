# Generated by Django 4.2.1 on 2023-07-16 08:57

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import products.models
import shortuuid.django_fields
import taggit.managers


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0001_initial"),
        ("taggit", "0005_auto_20220424_2025"),
        ("vendor", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CartOrder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=1.99, max_digits=15),
                ),
                ("paid_status", models.BooleanField(blank=True, default=False)),
                ("order_date", models.DateTimeField(auto_now_add=True)),
                (
                    "product_status",
                    models.CharField(
                        choices=[
                            ("processing", "Processing"),
                            ("shipped", "Shipped"),
                            ("delivered", "Delivered"),
                        ],
                        default="processing",
                        max_length=30,
                    ),
                ),
                (
                    "sku",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefgh12345",
                        blank=True,
                        length=5,
                        max_length=20,
                        null=True,
                        prefix="SKU",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Cart Order",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "pid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet=None,
                        length=22,
                        max_length=22,
                        prefix="",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(default="Fresh Pear", max_length=255)),
                (
                    "image",
                    models.ImageField(
                        default="product.jpg",
                        upload_to=products.models.user_directory_path,
                    ),
                ),
                (
                    "description",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, default=None, null=True
                    ),
                ),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=1.99, max_digits=15),
                ),
                (
                    "old_price",
                    models.DecimalField(decimal_places=2, default=2.99, max_digits=15),
                ),
                (
                    "specifications",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, null=True
                    ),
                ),
                (
                    "product_type",
                    models.CharField(
                        blank=True, default="Organic", max_length=100, null=True
                    ),
                ),
                ("stock_count", models.IntegerField(default=10)),
                (
                    "life_span",
                    models.CharField(
                        blank=True, default="100 Days", max_length=100, null=True
                    ),
                ),
                ("manufactured_date", models.DateTimeField(blank=True, null=True)),
                (
                    "product_status",
                    models.CharField(
                        choices=[
                            ("draft", "Draft"),
                            ("disabled", "Disabled"),
                            ("rejected", "Rejected"),
                            ("in_review", "In Review"),
                            ("published", "Published"),
                        ],
                        default="in_review",
                        max_length=10,
                    ),
                ),
                ("status", models.BooleanField(default=True)),
                ("featured", models.BooleanField(default=False)),
                ("digital", models.BooleanField(default=False)),
                (
                    "sku",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="1234567890",
                        length=4,
                        max_length=10,
                        prefix="sku",
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="product_categories",
                        to="core.category",
                    ),
                ),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        blank=True,
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Products",
            },
        ),
        migrations.CreateModel(
            name="ProductVariant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "var_id",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet=None, length=22, max_length=22, prefix="", unique=True
                    ),
                ),
                (
                    "variant_title",
                    models.CharField(default="Fresh Pear", max_length=255),
                ),
                (
                    "variant_color",
                    models.CharField(
                        blank=True, default="Red", max_length=100, null=True
                    ),
                ),
                (
                    "variant_size",
                    models.CharField(
                        blank=True, default="Large", max_length=100, null=True
                    ),
                ),
                (
                    "variant_image",
                    models.ImageField(
                        default="product.jpg",
                        upload_to=products.models.user_directory_path,
                    ),
                ),
                (
                    "variant_price",
                    models.DecimalField(decimal_places=2, default=1.99, max_digits=15),
                ),
                ("variant_stock_count", models.IntegerField(default=10)),
                (
                    "variant_type",
                    models.CharField(
                        blank=True, default="Organic", max_length=100, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Wishlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="products.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Wishlists",
            },
        ),
        migrations.CreateModel(
            name="ProductReview",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("review", models.TextField()),
                (
                    "rating",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (1, "★☆☆☆☆"),
                            (2, "★★☆☆☆"),
                            (3, "★★★☆☆"),
                            (4, "★★★★☆"),
                            (5, "★★★★★"),
                        ],
                        null=True,
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="reviews",
                        to="products.product",
                    ),
                ),
                (
                    "product_variant",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="variant_reviews",
                        to="products.productvariant",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Product Reviews",
            },
        ),
        migrations.CreateModel(
            name="ProductImages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "images",
                    models.ImageField(
                        default="product.jpg", upload_to="product-images"
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="product_images",
                        to="products.product",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Product Images",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="variants",
            field=models.ManyToManyField(
                related_name="products", to="products.productvariant"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="vendor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="vendor_products",
                to="vendor.vendor",
            ),
        ),
        migrations.CreateModel(
            name="CartOrderProducts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("invoice_no", models.CharField(max_length=200)),
                ("product_status", models.CharField(max_length=200)),
                ("item", models.CharField(max_length=200)),
                ("image", models.CharField(max_length=200)),
                ("qty", models.IntegerField(default=0)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=1.99, max_digits=15),
                ),
                (
                    "total",
                    models.DecimalField(decimal_places=2, default=1.99, max_digits=15),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.cartorder",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Cart Order Items",
            },
        ),
    ]
