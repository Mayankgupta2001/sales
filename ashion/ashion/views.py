from django.http import HttpResponse
from django.shortcuts import render


# menpage ko admin se redirect kiya 
from menpageapp.models import men_poster_carousel , men_poster_offer , men_product_carousel , men_product_collection ,men_bottom_poster

# womenpage ko admin se redirect kiya
from womenpageapp.models import women_poster_carousel , women_poster_offer ,women_product_collection ,women_product_carousel ,women_bottom_poster

# usersignup ko admin se redirect kiya
from usersignupapp.models import user_signup_data

# cartpage ko admin se redirect kiya
from cartpageapp.models import cartpage_data


def indexfn(request):
    return render(request , 'index.html')


def addresspagefn(request):
    return render(request , 'address-page.html')


def contactpagefn(request):
    return render(request , 'contactus-page.html')

def cartpagefn(request):
    cartpageData = cartpage_data.objects.all()

    d = {
        'cartpageData' : cartpageData
    }
    return render(request , 'cart-page.html',d)

def headerpagefn(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        rq=user_signup_data(name=name,email=email,password=password)
        rq.save()
    return render(request , 'header.html')

def menpagefn(request):
    posterimgData = men_poster_carousel.objects.all()
    offerimgData = men_poster_offer.objects.all()
    menproductimgData = men_product_carousel.objects.all()
    mencollectionData = men_product_collection.objects.all()
    menbottomimgData = men_bottom_poster.objects.all()

    d = {
        'posterimgData' : posterimgData,
        'offerimgData' : offerimgData,
        'menproductimgData' : menproductimgData,
        'mencollectionData' : mencollectionData,
        'menbottomimgData' : menbottomimgData
    }
    return render(request , 'men-page.html',d)

def paymentpagefn(request):
    return render(request , 'payment-page.html')

def womenpagefn(request):
    posterimgData = women_poster_carousel.objects.all()
    offerimgData = women_poster_offer.objects.all()
    womenproductimgData = women_product_carousel.objects.all()
    womencollectionData = women_product_collection.objects.all()
    womenbottomimgData = women_bottom_poster.objects.all()

    d = {
        'posterimgData' : posterimgData,
        'offerimgData' : offerimgData,
        'womenproductimgData' : womenproductimgData,
        'womencollectionData': womencollectionData,
        'womenbottomimgData' : womenbottomimgData


    }
    return render(request , 'women-page.html',d)

def popularpagefn(request):
    return render(request , 'popular-page.html')

def productpagefn(request):
    return  render(request , 'product-page.html')

def profilepagefn(request): 
    return render(request , 'profile-page.html')

def trackorderfn(request):
    return render(request , 'track-order.html')

