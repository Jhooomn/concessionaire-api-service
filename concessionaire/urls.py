from django.urls import path

from management import views

urlpatterns = [
    path('vehicles/save', views.save),
    path('vehicles/list', views.list),
    path('vehicles/update', views.update),
    path('vehicles/delete', views.delete)
]
