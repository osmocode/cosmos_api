from rest_framework import generics, mixins, permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer

class UserListView(mixins.ListModelMixin, generics.GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        return self.list(request)


class UserDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    
    queryset = User.objects.all()        
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )
    lookup_field = 'username'

    def get(self, request, *args, **kwargs):
        if kwargs.get(self.lookup_field) == 'me':
            return Response(self.get_serializer(request.user).data)
        return self.retrieve(request, *args, **kwargs)