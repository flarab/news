from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.api.views import NewsViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')
urlpatterns = []
urlpatterns += router.urls
