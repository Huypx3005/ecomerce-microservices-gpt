from django.urls import path
from .views import InventoryList, InventoryDetail

urlpatterns = [
    path("inventory/", InventoryList.as_view(), name="inventory-list"),
    path("inventory/<int:pk>/", InventoryDetail.as_view(), name="inventory-detail"),
]
