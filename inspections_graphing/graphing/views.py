import plotly.express as px

from django.shortcuts import render
from graphing.models import Graph

def chart(request):
    data = Graph.objects.all()
    
    fig = px.line(
        x=[d.name for d in data],
        y=[d.count for d in data],
        title="Inspections Graph",
        labels={'x': 'Name', 'y': 'Count'}
    )

    chart = fig.to_html()
    context = {'chart': chart}

    return render(request, 'graphing/graph.html', context)
