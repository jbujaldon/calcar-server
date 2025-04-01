from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status


class AccessTokenView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
    
        user = authenticate(email=email, password=password)
        
        if user is not None:
            tokens = _generate_jwt_for_user(user)
            return Response(tokens, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


def _generate_jwt_for_user(user):
    refresh = RefreshToken.for_user(user)
    
    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh),
        'has_onboarding_completed': user.has_onboarding_completed
    }
