from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import BookingViewSet, SingleMenuViewSet, MenuViewSet, home

urlpatterns = [
    path('menu/items/', MenuViewSet.as_view()),
    path('menu/items/<int:pk>/', SingleMenuViewSet.as_view()),

]
