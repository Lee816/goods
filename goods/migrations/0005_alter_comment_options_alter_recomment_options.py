# Generated by Django 4.2.7 on 2023-12-20 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_comment_recomment_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='recomment',
            options={'ordering': ['created_at']},
        ),
    ]