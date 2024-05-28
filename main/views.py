from django.shortcuts import render
from web3 import Web3
from .models import Transaction

# from rest_framework import Res
from rest_framework.response import Response

def buy_tokens(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
        account = w3.eth.accounts[0]
        token = w3.eth.contract(address=contract_address, abi=abi)
        token.functions.transfer(account, amount).transact({'from': account})
        Transaction.objects.create(amount=amount, type='buy')
        return Response("Token Buyed")
    else:
        return Response("Try to buy.")

def sell_tokens(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
        account = w3.eth.accounts[0]
        token = w3.eth.contract(address=contract_address, abi=abi)
        token.functions.transfer(contract_address, amount).transact({'from': account})
        Transaction.objects.create(amount=amount, type='sell')
        return Response("Sold Token.")
    else:
        return Response("Try to Sold Token.")

