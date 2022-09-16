from django.urls import path

from webapp.views import index_view, get_token_view,all_actions

app_name = 'webapp'

urlpatterns = [
    path('', index_view),
    path('add/', all_actions, name='all_actions'),
    path('subtract/', all_actions, name='all_actions'),
    path('multiply/', all_actions, name='all_actions'),
    path('divide/', all_actions, name='all_actions'),
    path('get_token/', get_token_view, name='get_token_view'),
]
