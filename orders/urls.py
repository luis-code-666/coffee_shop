from .views import MyOrderView
from django.urls import path


urlpatterns = [
    path ('mi-orden', MyOrderView.as_view(), name="my_order")
]
