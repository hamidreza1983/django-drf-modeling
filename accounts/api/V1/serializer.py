from rest_framework import serializers
from ...models import CustomeUser
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.contrib.auth import authenticate



class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255,write_only=True)

    class Meta:
        model = CustomeUser
        fields = ['email', 'username', 'password', 'password1']

    def validate(self, attrs):
        if attrs.get('password1') != attrs.get('password'):
            raise serializers.ValidationError(
                {
                'detail':'can not match password with confirmation password'
                }
            )

        try:

            validate_password(attrs.get('password'))
        
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(
                {
                'detail': list(e.messages)
                }
            )

        return super().validate(attrs)
    

    def create(self, validated_data):
        validated_data.pop('password1', None)
        return CustomeUser.objects.create_user(**validated_data)

class CustomSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=("email"),
        write_only=True
    )
    password = serializers.CharField(
        label=("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = ('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = ('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
