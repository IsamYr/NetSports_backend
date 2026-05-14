from datetime import date
from rest_framework import serializers

from NetSports import settings
from Users.models import Usuario, InfoPersonal, Profile


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50, allow_blank=False, allow_null=False, required=True)
    nombre = serializers.CharField(max_length=50, allow_blank=False, allow_null=False, required=True)
    apellidos = serializers.CharField(max_length=50, allow_blank=False, allow_null=False, required=True)
    email = serializers.EmailField(max_length=100, allow_blank=False, allow_null=False, required=True)
    telefono = serializers.CharField(max_length=11)
    password1 = serializers.CharField(min_length=8, allow_blank=False, allow_null=False, required=True)
    password2 = serializers.CharField(min_length=8, allow_blank=False, allow_null=False, required=True)
    fecha_nacimiento = serializers.DateField(allow_null=False, required=True)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'nombre', 'apellidos', 'telefono', 'password1', 'password2', 'fecha_nacimiento')

    def validate_username(self, username):
        if Usuario.objects.filter(username=username).exists():
            raise serializers.ValidationError("El usuario ya existe")
        return username


    def validate_email(self, email):
        if "@" not in email:
            raise serializers.ValidationError("El email no es válido")
        if any(ext in email for ext in settings.EXTENSIONES_BLACKLIST):
            raise serializers.ValidationError("Extensiones no permitidas: [" + ", ".join(settings.EXTENSIONES_BLACKLIST) + "]")

        if Usuario.objects.filter(email=email).exists():
            raise serializers.ValidationError("El correo ya existe. Pruebe con otro")

        return email

    def validate_password1(self, password):
        if not any(n.isdigit() for n in password):
            raise serializers.ValidationError("La contraseña debe de tener al menos un dígito")
        return password

    def validate_telefono(self, telefono):
        try:
            t = int(telefono)
            return telefono
        except:
            raise serializers.ValidationError("El número no es válido")

    def validate_fecha_nacimiento(self, fecha_nacimiento):
        actual_day = date.today()
        edad = actual_day.year - fecha_nacimiento.year
        if (actual_day.month, actual_day.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
            edad -= 1
        if edad < 18:
            raise serializers.ValidationError("Debes de ser mayor de edad para registrarte")
        return fecha_nacimiento

    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password1")
        validated_data.pop("password2")

        user = Usuario.objects.create(
            email = validated_data["email"],
            username = validated_data["username"],
        )
        user.set_password(password)
        user.save()

        InfoPersonal.objects.create(
            usuario=user,
            telefono=validated_data["telefono"],
            nombre=validated_data["nombre"],
            apellidos=validated_data["apellidos"],
            fecha_nacimiento=validated_data["fecha_nacimiento"],
        )

        Profile.objects.create(
            usuario=user,
        )

        return user