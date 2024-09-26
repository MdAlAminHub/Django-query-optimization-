from django.urls import path
from .views import (
    OrderListView, TotalRevenueView, OrderWithCustomerView, 
    OrderWithItemsView, CustomerOrdersView, OrdersWithoutItemsView
)

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('total-revenue/', TotalRevenueView.as_view(), name='total-revenue'),
    path('orders-with-customer/', OrderWithCustomerView.as_view(), name='orders-with-customer'),
    path('orders-with-items/', OrderWithItemsView.as_view(), name='orders-with-items'),
    path('customer-orders/<int:customer_id>/', CustomerOrdersView.as_view(), name='customer-orders'),
    path('orders-without-items/', OrdersWithoutItemsView.as_view(), name='orders-without-items'),
]
#sdhfsdfbjsfdbjsfjsfnjsddnfjsfnsnfsjfnsj