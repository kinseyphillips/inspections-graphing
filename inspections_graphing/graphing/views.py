import plotly.express as px
import csv

from django.shortcuts import render
from graphing.models import Graph
from django.http import JsonResponse
from django.conf import settings

def chart(request):
    if request.GET.get('attibute', None) is not None:
        attribute_name = request.GET.get('attribute_name')
    else:
        attribute_name = 'feature'
    
    datafile = settings.BASE_DIR / 'data' / '127-data.csv'
    data = {}

    with open(datafile, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if row[attribute_name] not in data:
                    data[row[attribute_name]] = 0
                data[row[attribute_name]] += 1

            for x in data:
                Graph.objects.get_or_create(name=x, count=data[x])

    df = Graph.objects.all()
    fig = px.pie(df, values=[d.count for d in df], names=[d.name for d in df])
    chart = fig.to_html()
    context = {'chart': chart}

    return render(request, 'graphing/graph.html', context)
