from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from places.models import Place


def show_mainpage(request):
    places = Place.objects.all()
    features = []
    for place in places:
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': place.get_coordinates()
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': 'static/places/moscow_legends.json'
            }
        }
        features.append(feature)

    data = {
        'type': 'FeatureCollection',
        'features': features
    }
    return render(request, 'mainpage.html', context={'data': data})


def show_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_data = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lon,
            'lat': place.lat
        }
    }
    return JsonResponse(place_data, safe=False, 
                        json_dumps_params={'ensure_ascii': False, 
                                           'indent': 4})
