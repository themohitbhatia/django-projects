# Generated by Django 4.1.4 on 2023-01-30 06:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_alter_productimage_image_alter_productimage_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="ColorVariant",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("color_name", models.CharField(max_length=100)),
                ("price", models.IntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SizeVariant",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("size_name", models.CharField(max_length=100)),
                ("price", models.IntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="product",
            name="color_variant",
            field=models.ManyToManyField(to="products.colorvariant"),
        ),
        migrations.AddField(
            model_name="product",
            name="size_variant",
            field=models.ManyToManyField(to="products.sizevariant"),
        ),
    ]
