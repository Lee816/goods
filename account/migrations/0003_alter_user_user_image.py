# Generated by Django 4.2.7 on 2023-11-27 08:01

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_followings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.ImageField(default='account/user.jpg', upload_to=account.models.user_image_path),
        ),
    ]
