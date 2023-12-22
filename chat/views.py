from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404

from .models import Room, Message


class RoomView(View):
    def get(self, request, pk):
        room = get_object_or_404(Room, id=pk)
        return render(request, "chat/room.html", {"room": room})
