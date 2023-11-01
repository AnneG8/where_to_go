from os import path
from urllib.parse import urlparse, unquote

import requests
from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Загружает локацию из json файла в БД'

    def add_arguments(self, parser):
        parser.add_argument(
            'json_urls',
            nargs='*',
            type=str,
            help='urls to JSON files'
        )

    def handle(self, *args, **options):
        for json_url in options['json_urls']:
            try:
                response = requests.get(json_url)
                response.raise_for_status()
                place_params = response.json()
            except requests.exceptions.HTTPError as err:
                CommandError(err)

            defaults = {
                'description_short': place_params['description_short'],
                'description_long': place_params['description_long'],
                'lat': place_params['coordinates']['lat'],
                'lon': place_params['coordinates']['lng'],
            }
            place, created = Place.objects.get_or_create(
                title=place_params['title'],
                defaults=defaults
            )

            for index, img_url in enumerate(place_params['imgs'], 1):
                try:
                    response = requests.get(img_url)
                    response.raise_for_status()
                    filepath = unquote(urlparse(img_url).path)
                    filename = path.split(filepath)[-1]
                    image, created = Image.objects.get_or_create(
                        place=place,
                        image=ContentFile(response.content, name=filename),
                        defaults={'image_num': place.images.count() + 1}
                    )
                except requests.exceptions.HTTPError:
                    continue
