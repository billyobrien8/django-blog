# Generated by Django 2.1.5 on 2020-11-17 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogging", "0002_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
    ]
