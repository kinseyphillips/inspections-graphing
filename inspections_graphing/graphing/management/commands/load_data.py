import csv

from django.conf import settings
from django.core.management.base import BaseCommand
from graphing.models import Graph

class Command(BaseCommand):
    help = 'Load data from inspection file'

    def handle(self, *args, **kwargs):
        datafile = settings.BASE_DIR / 'data' / '127-data.csv'
        features = []
        counter = {}

        with open(datafile, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                features.append(row['feature'])

        for x in features:
            if x not in counter:
                counter[x] = 0
            counter[x] += 1

        for key, value in counter.items():
            Graph.objects.get_or_create(name=key, count=value)