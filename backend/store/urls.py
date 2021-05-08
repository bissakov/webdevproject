from django.urls import path, include
from store import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('product-list/', views.ProductViewSet.as_view(), name='product-list'),
    path('product-list/<str:pk>/', views.ProductDetailViewSet.as_view(), name='product-detail'),
    path('category-list/', views.categoryViewSet, name='category-list'),
]