from django.urls import path
from .views import * 

app_name = "kakaopay"

urlpatterns = [
    path('', kakaoPay, name = 'kakaoPay'),
    path('kakaoPayLogic/', kakaoPayLogic),
    path('paySuccess/',paySuccess),
    path('payFail/',payFail),
    path('payCancel/',payCancel),
]
