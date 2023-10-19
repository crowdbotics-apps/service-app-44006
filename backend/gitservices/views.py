from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status


from .models import WebHook
# Create your views here.

class WebHookAPI(APIView):
    # permission_classes = [IsAuthenticated]
    parser_classes = [FormParser, MultiPartParser]

    def post(self, request, format=None):
        data = request.data
        if not data:
            return Response(data={}, status=status.HTTP_400_BAD_REQUEST)
        
        WebHook.objects.get_or_create(webhook_id=data["id"],
                                       defaults={"type":data["type"],
                                                "name": data["name"], 
                                                "events": str(data["events"])})
        return Response(data={}, status=status.HTTP_200_OK)
        
