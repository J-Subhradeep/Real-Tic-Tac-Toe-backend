from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import SecondClientSerializer
from .models import SecondClient
from rest_framework.response import Response
# Create your views here.


class JoinView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        values = SecondClient.objects.filter(
            group_name=data.get('group_name')).first()

        serializers = SecondClientSerializer(values)
        is_first = False
        if not values:
            is_first = True
        if serializers.data.get('first_client') and serializers.data.get('second_client'):
            bothClientPresent = True
        else:
            bothClientPresent = False
        return Response(dict(data=serializers.data, both=bothClientPresent, is_first=is_first))
