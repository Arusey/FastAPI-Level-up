from djangotuts.authentication.serializers import UserSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import jwt



from .models import User


# Create your views here.
class CreateUserAPIView(APIView):

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class LoginUser(APIView):

    def post(self, request):
        if not request.data:
            return Response(
                {
                    "error": "please provide an email and password"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        email = request.data['email']
        password = request.data['password']

        try:
            user = User.objects.get(email=email, password=password)
        except:
            return Response({
                "whoops": "Invalid email or password"
            },
            status=status.HTTP_400_BAD_REQUEST
            )
        
        if user:
            payload = {
                'email': user.email,
                'password': user.password
            }

            response_details = {
                'token': jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256"),
                'message': "Login successful",
                'status': status.HTTP_200_OK
            }

            return Response(response_details, status=response_details['status'])
        else:
            return Response({
                'error': 'Invalid credentials'
            },
            status=status.HTTP_400_BAD_REQUEST
            )



        





