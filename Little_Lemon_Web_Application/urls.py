from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from restaurant import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'menu-items', views.MenuViewSet, basename='menu-items')
# router.register(r'menu-items/(?P<pk>\d+)', views.SingleMenuViewSet, basename='single-menu-item')
router.register(r'booking', views.BookingViewSet, basename='booking')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', obtain_auth_token)
]

