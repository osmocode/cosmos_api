from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(('GET',))
def api_root(request):
    return Response({
        'auth-sign-in': reverse('cosmos_auth:sign-in', request=request),
        'auth-sign-out': reverse('cosmos_auth:sign-out', request=request),
        'auth-sign-refresh': reverse('cosmos_auth:sign-refresh', request=request),
    })
