from urllib import response
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from notifications.models import Notification
from notifications.serializers import NotificationSerializer

# Create your views here.

class ListNotifications(APIView):
    def get(self, request):
        queryset = Notification.objects.latest('sent').__dict__
        print(queryset)
        serializer = NotificationSerializer(data = queryset, context = {"request": request})
        serializer.is_valid()
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = NotificationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors)