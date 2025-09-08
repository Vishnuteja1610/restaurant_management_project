from django.shortcuts import render
from .models import ResturantInfo
from .forms import ContactForm

def contact_view(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_vaild():
         pass
    
    resturant = ResturantInfo.objects.first()
    return render(request,"contact.html",{"form":form,"resturant":resturant})
    