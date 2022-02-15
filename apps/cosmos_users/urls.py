from django.urls import path
from . import views

app_name = 'cosmos_users'

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='users-list'),
    path('users/<str:username>', views.UserDetailView.as_view(), name='users-detail')
]
