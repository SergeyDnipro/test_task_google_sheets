from django.contrib import admin
from google_sheets_extraction_app.models.Order import Order
from google_sheets_extraction_app.models.ExchangeRate import ExchangeRate

admin.site.register(Order)
admin.site.register(ExchangeRate)

