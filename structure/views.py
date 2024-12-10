from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from structure import models
from structure.models import Basket, Artwork
from users.models import User


# Create your views here.
def index(request):
    context = {
        'title': 'Soya Mariya Designer',
        'artworks1': models.Artwork.objects.all()[::3],
        'artworks2': models.Artwork.objects.all()[1::3],
        'artworks3': models.Artwork.objects.all()[2::3],
    }
    return render(request, 'structure/index.html', context )


def collections(request):
    context = {
        'title': 'Collection',
        'collections': models.Collection.objects.all()
    }
    return render(request, 'structure/collections.html', context)


def bio(request):
    context = { 'title': 'About me'}
    return render(request, 'structure/bio.html', context)


def universal_collect(request,collection_name):
    collection_id = models.Collection.objects.get(name=collection_name)
    sub_collection =  models.Artwork.objects.filter(collection=collection_id)
    return render(request, 'structure/universal_collect.html', {'result': sub_collection, 'collection': collection_name, 'title': collection_name})


def universal_year(request, year_name):
    year_id = models.Year.objects.get(year=year_name)
    by_year = models.Artwork.objects.filter(year=year_id)
    return render(request, 'structure/universal_year.html', {'result': by_year, 'year': year_name, 'title':year_name})


def artpiece(request, art_name):
    art_instance = get_object_or_404(models.Artwork, name=art_name)
    return render(request, 'structure/art.html', {'result': art_instance, 'art': art_name,'title': art_name })

def basket_add(request, product_id):
    artwork = Artwork.objects.get(id=product_id)
    user = User.objects.get(username=request.user)
    baskets = Basket.objects.filter(user=user, product=artwork)

    if not baskets.exists():
        Basket.objects.create(user=user, product=artwork, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_view(request):
    user = User.objects.get(username=request.user)
    context = {
        'baskets': Basket.objects.filter(user=user)
    }
    return render(request, 'structure/basket.html', context)


def basket_remove(request, id):
    basket = Basket.objects.get(pk=id)
    if basket.quantity == 1:
        basket.delete()
    else:
        basket.quantity -= 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
