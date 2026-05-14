import requests
from NetSports import settings

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class NutritionSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        query = request.GET.get("query")

        if not query:

            return Response({
                "success": False,
                "message": "Se necesita una query"
            }, status=status.HTTP_400_BAD_REQUEST)

        response = requests.get(
            "https://api.api-ninjas.com/v1/nutrition",
            params={
                "query": query
            },
            headers={
                "X-Api-Key": settings.NINJA_API_KEY
            }
        )

        return Response({
            "success": True,
            "data": response.json()
        }, status=status.HTTP_200_OK)