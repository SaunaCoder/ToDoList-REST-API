from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'todoitems', ToDoItemViewSet, basename='todoitem')

urlpatterns = [
    path('', include(router.urls)),
]
