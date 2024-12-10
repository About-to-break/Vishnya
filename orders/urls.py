from django.urls import path
from .views import OrderView, SuccessTemplateView, CancelTemplateView, OrderListView, order_remove, receipt_list_view

app_name = 'order'
urlpatterns = [
    path('', OrderView.as_view(), name='order_view'),
    path('success/', SuccessTemplateView.as_view(), name='success_order'),
    path('canсel/', CancelTemplateView.as_view(), name='cancel_order'),
    path('list/', OrderListView.as_view(), name='list_order'),
    path('list/remove/<int:id>', order_remove, name='order_remove'),
    path('receipt/<int:id>', receipt_list_view, name='receipt'),
]
