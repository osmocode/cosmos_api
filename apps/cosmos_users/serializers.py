from rest_framework.reverse import reverse
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    link = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'link',
            'username',
            'email',
            'password',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'last_login',
            'user_permissions'
        )

    def get_link(self, value):
        request = self.context['request']
        return reverse(
            'cosmos_users:users-detail',
            request=request,
            kwargs={'username': value.username}
        )