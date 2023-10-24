from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from evoapp.views import UserViewSet, PostViewSet, LikeAnalyticsView, home, LastRequestAnalytics

router = DefaultRouter()
router.register(r'users', UserViewSet)  # Registering UserViewSet with the router.
router.register(r'posts', PostViewSet)  # Registering PostViewSet with the router.

urlpatterns = [
    path('', home, name='home'),
    path("admin/", admin.site.urls),  # Admin panel URL.
    path("api/", include(router.urls)),  # Including all the API URLs registered with the router.
    path('api/user-activity/', LastRequestAnalytics.as_view(), name='user-activity'),
    path("api/analytics/", LikeAnalyticsView.as_view(), name='likes-analytics'),  # Analytics API endpoint.
]



