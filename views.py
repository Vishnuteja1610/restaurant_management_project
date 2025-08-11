from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):
    try:
        context = {
            'resturant_name':'Nothing Before Milkshake',
            'welcome_message':'Welcome to our milkshake paradise!'
            'current_year':datetime.now().current_year
        }
        return render(request, 'home.html', context)
    except Exception as e:

        return HttpResponse(f"An error occurred: {str(e)}", status=500)