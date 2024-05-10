import csv

from django.conf import settings
from django.core.management.base import BaseCommand
from graphing.models import Graph

class Command(BaseCommand):
    help = 'Load data from inspection file'

    def handle(self, *args, **kwargs):
        datafile = settings.BASE_DIR / 'data' / '127-data.csv'
        counter = {}

        with open(datafile, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if row['feature'] not in counter:
                    counter[row['feature']] = 0
                counter[row['feature']] += 1

            for x in counter:
                Graph.objects.get_or_create(name=x, count=counter[x])