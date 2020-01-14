from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, ChatSerializer
# from rest_framework.parsers import JSONParser
from .models import User, ChatHistory
from rest_framework.response import Response
import re, datetime, time, requests

api_key = 'p87dtt61i4'


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
                # print(request.data['msg'])
                if 'msg' in request.data:
                    # dialog flow logic
                    # Live train status

                    print(request.data['msg'])
                    try:
                        trn_no = str(re.search(r'\d+', request.data['msg']).group())

                    except:
                        trn_no = None

                    date = str(re.search(r'\d{2}-\d{2}-\d{4}', request.data['msg']).group())

                    d_station = request.data['msg'].split('from ')
                    station = (d_station[1])

                    # call railway api

                    url = "https://api.railwayapi.com/v2/live/train/" + trn_no + "/station/" + station + "/date/" + date + "/apikey/" + api_key + "/"
                    print(url)
                    get_status = requests.get(url).json()
                    print(get_status)

                    qw = get_status["position"]
                    print(qw)

                    solution = "You queried for Train: " + str(qw)

                    request.data['reply'] = solution
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
