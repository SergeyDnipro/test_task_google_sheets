import requests
import ccy
from google_sheets.celery import app
from google_sheets_extraction_app.models.ExchangeRate import ExchangeRate
import datetime


@app.task
def exchange_rate(from_currency, to_currency):

    response = requests.get('https://api.monobank.ua/bank/currency')
    data = response.json()
    from_currency_code = int(ccy.currency(from_currency).isonumber)
    to_currency_code = int(ccy.currency(to_currency).isonumber)
    currency_table = [i for i in data if i['currencyCodeA'] == from_currency_code and i['currencyCodeB'] == to_currency_code][0]
    currency_rate_value = (currency_table['rateBuy'] + currency_table['rateSell']) / 2
    currency_rate_date = datetime.datetime.fromtimestamp(currency_table['date'])

    ExchangeRate.objects.update_or_create(
        from_code=from_currency_code,
        to_code=to_currency_code,
        defaults={
            'rate': currency_rate_value,
            'date_of_rate': currency_rate_date,
        }
    )
    print(f'Exchange rate refreshes at {datetime.datetime.now()}')
