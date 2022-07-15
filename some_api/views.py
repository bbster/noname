from rest_framework import status
from rest_framework.response import Response
from .models import Some_Table
from rest_framework.views import APIView

from .serializers import SomeSerializer


class SomeList(APIView):
    def get(self, request):
        some_list = SomeSerializer(Some_Table.objects.all(), many=True)

        return Response(data=some_list.data, status=status.HTTP_200_OK)
