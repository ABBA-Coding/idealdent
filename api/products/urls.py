from django.urls import path

from api.products import views

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category-list'),
    path('<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('subcategories/<int:pk>/', views.SubCategoryDetailView.as_view(), name='subcategory-detail'),
]