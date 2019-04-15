from django.shortcuts import render
from .models import SubscribersForms, Subscriber
from products.models import ProductImage

# Create your views here.
def landing(request):
    name = "CodingMethod"
    current_day = "03.01.2017"
    
    form = SubscribersForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
#        print(request.POST)
        print(form.cleaned_data.get('email'))
        for subs in Subscriber.objects.all():
            print(subs.name)
        form.save() 
        
    return render(request, "landing/landing.html",locals())



def home(request):
    products = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, "landing/home.html", locals())



















