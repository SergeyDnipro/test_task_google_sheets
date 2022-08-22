from datetime import datetime, date
from google_sheets.celery import app
from google_sheets_extraction_app.models.Order import Order
from google_sheets_extraction_app.functions.get_google_sheets import get_google_sheets
from google_sheets_extraction_app.tasks.msg_to_telegram import msg_to_telegram
from google_sheets_extraction_app.models.ExchangeRate import ExchangeRate


@app.task
def update_data():
    table_values = get_google_sheets()
    processed_ids = []

    for element in table_values:
        try:
            order, updated = Order.objects.update_or_create(
                order_id=element['order_id'],
                defaults={
                    'excel_id': element['excel_id'],
                    'price_usd': element['price_usd'],
                    'price_uah': element['price_uah'] * ExchangeRate.objects.first().rate,
                    'delivery_date': datetime.strptime(element['delivery_date'], '%d.%m.%Y').date()
                }
            )

            assert isinstance(order, Order)
            processed_ids.append(order.order_id)

            if order.delivery_date < date.today() and order.msg_status is False:
                order.msg_status = True
                order.msg_status_text = 'Expired'
                order.save(update_fields=['msg_status', 'msg_status_text'])
                msg_to_telegram.delay(f'Order due date expired: {order.order_id} - ${order.price_usd}')

            # Delivery date may be changed for future date manually in original google sheets
            elif order.delivery_date > date.today() and order.msg_status is True:
                order.msg_status = False
                order.msg_status_text = 'In process...'
                order.save(update_fields=['msg_status', 'msg_status_text'])

        except ValueError:  # Google sheets cell has incorrect values, typing by users
            print(f'Value Error in order #{order.order_id}')

    Order.objects.exclude(order_id__in=processed_ids).delete()
    print('DB refreshes with original google sheets')
