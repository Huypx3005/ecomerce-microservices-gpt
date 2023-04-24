import requests
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer


class PaymentView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        # Call third-party payment gateway API to process the payment
        amount = request.data.get("amount")
        card_number = request.data.get("card_number")
        card_exp_month = request.data.get("card_exp_month")
        card_exp_year = request.data.get("card_exp_year")
        card_cvv = request.data.get("card_cvv")

        # Make API request to third-party payment gateway
        response = requests.post(
            "https://third-party-payment-gateway.com/process-payment",
            data={
                "amount": amount,
                "card_number": card_number,
                "card_exp_month": card_exp_month,
                "card_exp_year": card_exp_year,
                "card_cvv": card_cvv,
            },
        )

        # Check the response from the payment gateway
        if response.status_code == 200:
            # Payment was successful, save the payment details in the database
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        else:
            # Payment failed, return an error response
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
