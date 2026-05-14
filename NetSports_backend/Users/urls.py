from django.urls import path

from Users.views import LoginView, RegisterView, UsersView, MyProfileView, ProfileView, MyInfoPersonalView, \
    UsersSearchView, UpdateMyInfoPersonalView, UpdateMyProfileView

urlpatterns = [
    path('registro/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    # path('usuarios/', UsersView.as_view()),
    path('usuarios/search/', UsersSearchView.as_view()),
    path('mi-perfil/', MyProfileView.as_view()),
    path('mi-perfil/update/', UpdateMyProfileView.as_view()),
    path('mi-perfil/informacion_personal/', MyInfoPersonalView.as_view()),
    path('mi-perfil/informacion-personal/update/', UpdateMyInfoPersonalView.as_view()),
    # path('perfiles/', ProfileView.as_view()),
    path('perfiles/<str:username>/', ProfileView.as_view()),
]