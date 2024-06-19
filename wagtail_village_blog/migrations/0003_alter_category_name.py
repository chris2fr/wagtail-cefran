# Generated by Django 5.0.6 on 2024-06-18 14:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wagtail_village_blog", "0002_alter_category_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=80, unique=True, verbose_name="Category name"),
        ),
    ]