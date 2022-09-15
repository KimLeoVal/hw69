from django.urls import path

from webapp.views import add_numbers, index_view, get_token_view, subtract_numbers, multiply_numbers, divide_numbers

app_name = 'webapp'

urlpatterns = [
    path('', index_view),
    path('add/', add_numbers, name='add_numbers'),
    path('subtract/', subtract_numbers, name='subtract_numbers'),
    path('multiply/', multiply_numbers, name='multiply_numbers'),
    path('divide/', divide_numbers, name='divide_numbers'),
    path('get_token/', get_token_view, name='get_token_view'),
]
