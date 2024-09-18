from django.urls import path
from .views import numbers, sum_numbers

urlpatterns = [
    path('api/numbers/', numbers, name='numbers'),
    path('api/sum/', sum_numbers, name='sum_numbers'),
]