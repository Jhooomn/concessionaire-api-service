from django.conf.urls import url, include
from rest_framework import routers

from management import views

router = routers.DefaultRouter()
router.register(r'vehicles', views.VehicleViewSet)
urlpatterns = [
    url(r'^', include(router.urls))
]
