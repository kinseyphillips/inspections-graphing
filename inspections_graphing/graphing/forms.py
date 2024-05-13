from django import forms
from .models import Graph

class GraphForm(forms.ModelForm):
    class Meta:
        model = Graph
        fields = ['name', 'count']

        def __init__(self, *args, **kwargs):
            super().__inint__(*args, **kwargs)
            self.fields['name'].widget.attrs.update({"class": "form-control"})

            for field in self.fields:
                self.fields[field].widget.attrs.update({"class": "form-control"})