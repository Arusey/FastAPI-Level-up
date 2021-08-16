from django.urls import path
from django.conf.urls import url
from .views import CreateUserAPIView, LoginUser

urlpatterns = [
    path('user/create_user/', CreateUserAPIView.as_view(), name="register"),
    path('user/login/', LoginUser.as_view(), name="login")
]