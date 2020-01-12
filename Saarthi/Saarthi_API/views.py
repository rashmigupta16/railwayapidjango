from django.shortcuts import render

# Create your views here.
from rest_framework import generics
# from rest_framework import viewsets
from .serializers import UserSerializer, ChatSerializer
# from rest_framework.parsers import JSONParser
from .models import User, ChatHistory
from rest_framework.response import Response


class UserCreateApi(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        if 'HTTP_SECRET' in request.META:
            if request.META['HTTP_SECRET'] == 'rashmii':
                return self.create(request)
            else:
                data = {
                    'message': 'invalid Key'
                }
                return Response(status=404, data=data)
        else:
            data = {
                'message': 'header not found'
            }
            return Response(status=404, data=data)


class UserList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        if 'HTTP_SECRET' in request.META:
            if request.META['HTTP_SECRET'] == 'rashmii':
                self.queryset = User.objects.all()
                return self.list(request, *args, **kwargs)
            else:
                data = {
                    'message': 'invalid Key'
                }
                return Response(status=404, data=data)
        else:
            data = {
                'message': 'header not found'
            }
            return Response(status=404, data=data)


class ChatHistoryCreateApi(generics.CreateAPIView):
    serializer_class = ChatSerializer

    def post(self, request, *args, **kwargs):
        if 'HTTP_SECRET' in request.META:
            if request.META['HTTP_SECRET'] == 'rashmii':
                print(request.data['msg'])
                if 'msg' in request.data:
                    # dialog flow logic
                    # call railway api
                    request.data['reply'] ='solution'
                    return self.create(request)
            else:
                data = {
                    'message': 'invalid Key'
                }
                return Response(status=404, data=data)
        else:
            data = {
                'message': 'header not found'
            }
            return Response(status=404, data=data)
