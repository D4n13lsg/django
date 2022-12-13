from django.urls import path
from .views import MotoListApiView

urlpatterns = [
    path('', MotoListApiView.as_view(), name="Moto_list"),
    path('<int:moto_id>/', MotoListApiView.as_view(), name="Moto_detail"),
]