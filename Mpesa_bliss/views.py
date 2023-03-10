from __future__ import unicode_literals
from django.shortcuts import render
from django_daraja.mpesa import utils
from django.views.generic import View
from django_daraja.mpesa.core import MpesaClient
from decouple import config
from datetime import datetime
from django.http import HttpResponse, JsonResponse

cl = MpesaClient()
stk_pus_callback_url = 'https://api.darajambili.com/express-payment'
b2c_callback_url = 'https://api.dajarambili.com/b2c/result'


def oauth_success(request):
    r = cl.access_token()
    return JsonResponse(r, safe=False)


def index(request):
    if request.method == 'POST':
        phone_no = request.POST.get('phone')
        amount = request.POST.get('amount')
        amount = int(amount)
        account_Reference = 'Bliss'
        transaction_desc = 'STK Push Description'
        callback_url = stk_pus_callback_url
        r = cl.stk_push(phone_no, amount, account_Reference, transaction_desc, callback_url)
        return JsonResponse(r.response_description, safe=False)

    return render(request, 'index.html')
