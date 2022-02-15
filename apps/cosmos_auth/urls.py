from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserSignOutView

app_name = 'cosmos_auth'

urlpatterns = [
    path('auth/sign-in/', TokenObtainPairView.as_view(), name='sign-in'),
    path('auth/sign-out/', UserSignOutView.as_view(), name='sign-out'),
    path('auth/sign-refresh/', TokenRefreshView.as_view(), name='sign-refresh'),
]
