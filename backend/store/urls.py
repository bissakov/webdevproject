from django.urls import path, include
from store import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('product-list/', views.ProductViewSet.as_view(), name='product-list'),
    path('product-list/<str:pk>/', views.ProductDetailViewSet.as_view(), name='product-detail'),
    path('category-list/', views.categoryViewSet, name='category-list'),
]