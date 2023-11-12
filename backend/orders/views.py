from django.shortcuts import render
from rest_framework.views import APIView, Response
from django.http import HttpResponse


class Index(APIView):
    def get(self, request):
        print(request.user)
        return Response({'message': 'Hi, bro!'})
