from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailOrPhoneBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        user = UserModel.objects.filter(email=username).first() or UserModel.objects.filter(
            info_personal__telefono=username).first()

        if user and user.check_password(password):
            return user

        return None