# Generated by Django 5.0 on 2024-02-26 13:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("goods", "0006_alter_design_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="goods",
            options={"ordering": ["-created_at"]},
        ),
    ]