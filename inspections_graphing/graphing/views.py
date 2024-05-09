import plotly.express as px

from django.shortcuts import render
from graphing.models import Graph

def pie_graph(request):
    data = Graph.objects.all()
    
    print(data)
    """
    fig = px.pie(values=data.count, names=data.name)

    pie_graph = fig.to_html()
    context = {'pie_graph': pie_graph}

    return render(request, 'graphing/graph.html', context)
    """
    return(request)
