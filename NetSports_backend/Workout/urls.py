from django.urls import path

from Workout.views import ExerciseView, RoutineView, AddExerciseToRoutineView, CreateRoutineView, RemoveExerciseFromRoutineView, DeleteRoutineView

urlpatterns = [
    path('ejercicios/', ExerciseView.as_view()),
    path('rutinas/', RoutineView.as_view()),
    path('rutinas/<int:routine_id>/remove-routine/', DeleteRoutineView.as_view()),
    path('rutinas/<int:routine_id>/add-exercise/', AddExerciseToRoutineView.as_view()),
    path('rutinas/<int:routine_id>/remove-exercise/', RemoveExerciseFromRoutineView.as_view()),
    path('rutinas/create/', CreateRoutineView.as_view()),
]