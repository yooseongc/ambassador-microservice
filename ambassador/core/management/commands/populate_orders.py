from django.core.management import BaseCommand
from core.models import Order
from django.db import connections


class Command(BaseCommand):
    def handle(self, *args, **options):

        with connections['old'].cursor() as cursor:
            cursor.execute('SELECT id, user_id, code FROM core_order WHERE complete = 1')
            orders = cursor.fetchall()

            for order in orders:
                cursor.execute(f"SELECT ambassador_revenue FROM core_orderitem WHERE order_id = '{order[0]}'")
                order_items = cursor.fetchall()
                Order.objects.create(
                    id=order[0],
                    user_id=order[1],
                    code=order[2],
                    total=sum(item[0] for item in order_items)
                )

