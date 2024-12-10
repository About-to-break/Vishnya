from django.urls import path
from structure.views import *

app_name = 'structure'
urlpatterns = [
    path('', index, name='index'),
    path('collections/', collections, name='collections'),
    path('sub_collection/<str:collection_name>/', universal_collect, name='universal_collect'),
    path('by_year/<str:year_name>/',universal_year, name='universal_year'),
    path('art_instance/<str:art_name>/', artpiece, name='artpiece'),
    path('about/', bio, name='bio'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/view/', basket_view, name='basket_view'),
    path('baskets/remove/<int:id>/', basket_remove, name='basket_remove'),
]