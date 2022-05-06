from django.urls import path
from .views import (
    get_data,
    receive_data,
    send_setup,
    send_data,
    test
)

urlpatterns = [
    path('', get_data, name='sensors_home'),
    path('receive_data/', receive_data, name='receive_data'),
    path('send_setup/', send_setup, name='send_setup'),
    path('send_data/', send_data, name='send_data'),
    path('test/', test, name='test') # TODO delete this
]
