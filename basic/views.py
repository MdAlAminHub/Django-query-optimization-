from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order, OrderItem, Customer

# 1. Annotating total quantity per order
class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.annotate(total_quantity=Sum('items__quantity'))
        result = [
            {
                "order_id": order.id,
                "customer_name": order.customer.name,
                "total_quantity": order.total_quantity
            }
            for order in orders
        ]
        return Response(result)

# 2. Aggregating total revenue for all orders
class TotalRevenueView(APIView):
    def get(self, request):
        total_revenue = OrderItem.objects.aggregate(total=Sum('product__price'))
        return Response(total_revenue)

# 3. Retrieving orders with customer details (select_related)
class OrderWithCustomerView(APIView):
    def get(self, request):
        orders = Order.objects.select_related('customer').all()
        result = [
            {
                "order_id": order.id,
                "customer_name": order.customer.name,
                "customer_email": order.customer.email
            }
            for order in orders
        ]
        return Response(result)

# 4. Prefetching order items for each order (prefetch_related)
class OrderWithItemsView(APIView):
    def get(self, request):
        orders = Order.objects.prefetch_related('items').all()
        result = [
            {
                "order_id": order.id,
                "items": [
                    {
                        "product_name": item.product.name,
                        "quantity": item.quantity
                    } for item in order.items.all()
                ]
            }
            for order in orders
        ]
        return Response(result)

# 5. Filtering orders by customer
class CustomerOrdersView(APIView):
    def get(self, request, customer_id):
        customer_orders = Order.objects.filter(customer_id=customer_id)
        result = [
            {
                "order_id": order.id,
                "created_at": order.created_at
            }
            for order in customer_orders
        ]
        return Response(result)

# 6. Excluding orders with no items
class OrdersWithoutItemsView(APIView):
    def get(self, request):
        orders = Order.objects.exclude(items__isnull=True)
        result = [
            {
                "order_id": order.id,
                "customer_name": order.customer.name
            }
            for order in orders
        ]
        return Response(result)

