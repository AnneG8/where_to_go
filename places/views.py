from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from places.models import Place


def show_mainpage(request):
    places = Place.objects.all()
    features = [{
                    'type': 'Feature',
                    'geometry': {
                        'type': 'Point',
                        'coordinates': place.get_coordinates()
                    },
                    'properties': {
                        'title': place.title,
                        'placeId': place.id,
                        'detailsUrl': reverse('place', kwargs={'place_id': place.id})
                    }
                } for place in places]
    geo_json = {
        'type': 'FeatureCollection',
        'features': features
    }
    return render(request, 'mainpage.html', context={'geo_json': geo_json})


def show_place(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related('images'), id=place_id)
    serialize_place = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'short_description': place.short_description,
        'long_description': place.long_description,
        'coordinates': {
            'lng': place.lon,
            'lat': place.lat
        }
    }
    return JsonResponse(serialize_place, safe=False, 
                        json_dumps_params={'ensure_ascii': False, 
                                           'indent': 4})
