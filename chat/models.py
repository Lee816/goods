from django.db import models

from account.models import User


class Room(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user1_room")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2_room")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["-created_at"]),
            models.Index(fields=["user1"]),
            models.Index(fields=["user2"]),
        ]

    def __str__(self):
        return f"{self.user1} - {self.user2}의 채팅방"


class Message(models.Model):
    message = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="message")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
        indexes = [
            models.Index(fields=["created_at"]),
            models.Index(fields=["sender"]),
            models.Index(fields=["room"]),
        ]

    def __str__(self):
        return f"{self.sender}이 보낸 메세지"
