from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from Users.models import Usuario


class UsersSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        search_term = request.query_params.get('username', '').strip()

        if not search_term or len(search_term) < 2:
            return Response([], status=status.HTTP_200_OK)

        usuarios = Usuario.objects.filter(
            Q(username__icontains=search_term) |
            Q(email__icontains=search_term)
        ).values('id', 'username', 'email', 'slug')[:10]  # Limita a 10 resultados


        return Response(list(usuarios), status=status.HTTP_200_OK)