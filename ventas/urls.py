from django.urls import path, include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'ventas', views.VentasViewSet, basename = 'ventas')


urlpatterns = [
    path('', include(router.urls)),

]
