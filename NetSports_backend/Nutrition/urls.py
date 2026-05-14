from django.urls import path

from Nutrition.views import NutritionSearchView

urlpatterns = [
    path('nutrition/search/', NutritionSearchView.as_view()),
]