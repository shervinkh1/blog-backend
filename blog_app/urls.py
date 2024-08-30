# blog/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet

router = DefaultRouter()
router.register(r'blog', BlogViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
]
