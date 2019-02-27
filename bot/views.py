from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView

from bot import bot_vk
from bot.models import Player


class VkView(APIView):
    queryset = Player.objects.all()

    def post(self, request):
        if request.data['type'] == 'confirmation':
            return HttpResponse('e1511323', status=status.HTTP_200_OK)

        bot_vk.handle_incoming_message(request.data)
        return HttpResponse('ok', status=status.HTTP_200_OK)
