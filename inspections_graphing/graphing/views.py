import plotly.express as px

from django.shortcuts import render
from graphing.models import Graph

def chart(request):
    df = Graph.objects.all()
    
    fig = px.pie(df, values=[d.count for d in df], names=[d.name for d in df])

    chart = fig.to_html()
    context = {'chart': chart}

    return render(request, 'graphing/graph.html', context)
