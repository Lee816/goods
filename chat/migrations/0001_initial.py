# Generated by Django 5.0 on 2023-12-22 16:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user1_room",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user2_room",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Message",
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
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiver_message",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sender_message",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="message",
                        to="chat.room",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.AddIndex(
            model_name="room",
            index=models.Index(
                fields=["-created_at"], name="chat_room_created_cc8caf_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="room",
            index=models.Index(fields=["user1"], name="chat_room_user1_i_f80515_idx"),
        ),
        migrations.AddIndex(
            model_name="room",
            index=models.Index(fields=["user2"], name="chat_room_user2_i_d30f1a_idx"),
        ),
        migrations.AddIndex(
            model_name="message",
            index=models.Index(
                fields=["-created_at"], name="chat_messag_created_f18bb8_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="message",
            index=models.Index(
                fields=["sender"], name="chat_messag_sender__c4389c_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="message",
            index=models.Index(
                fields=["receiver"], name="chat_messag_receive_b6ffa6_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="message",
            index=models.Index(fields=["room"], name="chat_messag_room_id_cee780_idx"),
        ),
    ]
