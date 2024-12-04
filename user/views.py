from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import AllowAny


class RegisterView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Create a token for the user
            token, _ = Token.objects.get_or_create(user=user)

            return Response(
                {"message": "User registered successfully!",  "token": token.key}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token, _ = Token.objects.get_or_create(user=serializer.validated_data['user'])
        return Response({"token": token.key, "message": "Login successful!"}, status=status.HTTP_200_OK)    


class LogoutView(APIView):

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response(
                {"message": "Successfully logged out."},
                status=status.HTTP_200_OK
            )
        except Token.DoesNotExist:
            return Response(
                {"error": "Token not found or already logged out."},
                status=status.HTTP_400_BAD_REQUEST
            )

            
    