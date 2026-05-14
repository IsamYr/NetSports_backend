from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from Users.models import Usuario


class UsersView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        users = Usuario.objects.all()
        data = []

        for user in users:
            data.append({
                'username': user.username,
                'email': user.email,
            })

        return Response({'data': data}, status=status.HTTP_200_OK)