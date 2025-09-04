from django.shortcuts import render
import random

def order_confirmation(request,order_id):
    return render(request,"order_confirmation.html",{"order_id":order_id})