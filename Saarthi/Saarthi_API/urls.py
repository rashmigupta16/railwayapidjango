from django.urls import path
from . import views

urlpatterns = [
    path('users_create', views.UserCreateApi.as_view(), name='users_create'),
    path('chat_history', views.ChatHistoryCreateApi.as_view(), name='history'),
    path('view_user', views.UserList.as_view(), name='user_view'),

]
