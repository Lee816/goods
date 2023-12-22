from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from django.db.models import Q

from account.models import User
from .models import Room, Message


class RoomView(View):
    def get(self, request, pk):
        opponent = get_object_or_404(User, id=pk)
        room = Room.objects.filter(
            Q(user1=request.user, user2=opponent)
            | Q(user2=request.user, user1=opponent)
        )
        if len(room) == 1:
            messages = Message.objects.filter(room=room[0])

            return render(
                request, "chat/room.html", {"room": room[0], "messages": messages}
            )
        else:
            raise ValueError("Room Error")
