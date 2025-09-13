from django.shortcuts import render

def home(request):
    context = {
        "title":"Welcome to Spice Haven - Authentic Flavors in Hyderabad",
        "restaurant-name":"Spice Haven",
        "location":"Hyderabad",
    }
    return render(request,"home.html",context)