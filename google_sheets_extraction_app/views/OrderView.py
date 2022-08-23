from rest_framework import generics
from google_sheets_extraction_app.models.ExchangeRate import ExchangeRate
from google_sheets_extraction_app.serializers.OrderSerializer import OrderSerializer
from django.template.response import TemplateResponse
from google_sheets_extraction_app.models.Order import Order


class OrderView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


def order_view(request):
    return TemplateResponse(request, 'orders/orders_js.html', {
        'current_data': ExchangeRate.objects.first()
    })
