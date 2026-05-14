from rest_framework_simplejwt.tokens import RefreshToken

from NetSports import settings
from Users.models import Usuario
from rest_framework import serializers

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100, allow_null=True, allow_blank=True, required=False)
    telefono = serializers.CharField(max_length=11, allow_null=True, allow_blank=True, required=False)
    password = serializers.CharField(required=True, allow_null=False, allow_blank=False, min_length=8)

    class Meta:
        model = Usuario
        fields = ('email', 'password', 'telefono')

    def validate_password(self, password):
        if not any(n.isdigit() for n in password):
            raise serializers.ValidationError("La constraseña es incorrecta")
        return password

    def validate(self, attrs):
        email = attrs.get('email')
        telefono = attrs.get('telefono')
        password = attrs.get('password')

        if not email and not telefono:
            raise serializers.ValidationError("No hay correo / No hay teléfono")


        if email:
            user = Usuario.objects.filter(email=email).first()
            if "@" not in email:
                raise serializers.ValidationError("El formato de correo es incorrecto")
            if "=" in email:
                raise serializers.ValidationError("No es válido el carácter '='")
            if any(ext in email for ext in settings.EXTENSIONES_BLACKLIST):
                raise serializers.ValidationError("La extensión no es válida")

            if not user:
                raise serializers.ValidationError("El usuario no existe")
            else:
                if not user.check_password(password):
                    raise serializers.ValidationError("La contraseña no es válida")
            refresh = RefreshToken.for_user(user)

        else:
            user = Usuario.objects.filter(info_personal__telefono=telefono).first()
            try:
                t = int(telefono)
                if t < 0:
                    raise serializers.ValidationError("No hay teléfono")
                if not user:
                    raise serializers.ValidationError("El usuario no existe")
                else:
                    if not user.check_password(password):
                        raise serializers.ValidationError("La contraseña no es válida")
                refresh = RefreshToken.for_user(user)

            except:
                raise serializers.ValidationError("El telefono no es válido")


        return {
            "success": True,
            "data": {
                "email": user.email,
                "username": user.username,
                "nombre": getattr(user.info_personal, "nombre", None),
                "apellidos": getattr(user.info_personal, "apellidos", None),
                "fecha_union": getattr(user.info_personal, "fecha_union", None),
                "refreshToken": str(refresh),
                "token": str(refresh.access_token),
            }
        }