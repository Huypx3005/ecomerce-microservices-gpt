from rest_framework import generics
import requests
from .models import Inventory
from .serializers import InventorySerializer


class InventoryList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def perform_create(self, serializer):
        # Call the product catalog microservice to get the product details
        product_id = serializer.validated_data["product_id"]
        product_url = f"http://localhost:8000/products/{product_id}/"
        response = requests.get(product_url)
        product_data = response.json()

        # Add the product name and price to the order
        serializer.validated_data["product_name"] = product_data["name"]
        serializer.validated_data["product_price"] = product_data["price"]

        # Create the order
        serializer.save()


class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
