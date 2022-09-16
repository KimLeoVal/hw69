from django.urls import path

from webapp.views import index_view, get_token_view, all_actions, TestView, CreateTest

app_name = 'webapp'

urlpatterns = [
    path('', index_view),
    path('add/', all_actions, name='add'),
    path('subtract/', all_actions, name='subtract'),
    path('multiply/', all_actions, name='multiply'),
    path('divide/', all_actions, name='divide'),
    path('get_token/', get_token_view, name='get_token_view'),
    path('test/', TestView.as_view(), name='TestView'),
    path('create/', CreateTest.as_view(), name='CreateTest'),
]
