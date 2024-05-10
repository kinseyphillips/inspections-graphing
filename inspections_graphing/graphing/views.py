import plotly.express as px

from django.shortcuts import render
from graphing.models import Graph

def chart(request):
    Graph.objects.get_or_create(name='Other', count=0)
    df = Graph.objects.all()
    o = Graph.objects.get(name='Other')
    #other = {}
        
    total = 0
    for x in df:
        total += x.count
    min = total * 0.05

    tmp = 0
    for d in df:
        if d.count < min:
            # other.update({d.name : d.count})
            o.count += d.count
            # o = Graph.objects.get(name='Other')
            # tmp = o.count + d.count
            # o.count = tmp
            o.save()
            
           

    fig = px.pie(df, values=[d.count for d in df], names=[d.name for d in df])
    chart = fig.to_html()
    context = {'chart': chart}

    return render(request, 'graphing/graph.html', context)
