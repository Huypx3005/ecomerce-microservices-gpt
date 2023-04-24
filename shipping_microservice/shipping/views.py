# views.py

import requests
from rest_framework import generics
from rest_framework.response import Response
from .models import ShippingAddress, Shipment
from .serializers import ShippingAddressSerializer, ShipmentSerializer


class ShippingAddressList(generics.ListCreateAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer


class ShippingAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer


class ShipmentList(generics.ListCreateAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer


class ShipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer


class ShippingRate(generics.GenericAPIView):
    def get(self, request):
        # make an API call to an external shipping provider to calculate shipping rates based on weight, dimensions, origin, and destination
        response = requests.get(
            "https://example.com/shipping/rates", params=request.query_params
        )
        if response.status_code == 200:
            return Response(response.json())
        else:
            return Response({"error": "Failed to retrieve shipping rates"})


class ShippingLabel(generics.GenericAPIView):
    def post(self, request):
        # make an API call to an external shipping provider to generate a shipping label
        response = requests.post(
            "https://example.com/shipping/label", data=request.data
        )
        if response.status_code == 200:
            return Response(response.json())
        else:
            return Response({"error": "Failed to generate shipping label"})


# class ShipmentTracking(generics.GenericAPIView):
#     def get(self, request, tracking_number):
