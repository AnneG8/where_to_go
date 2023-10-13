from django.shortcuts import render
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
