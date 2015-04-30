from django.views.generic import TemplateView

from rest_framework import viewsets

from .serializers import (
    LabelSerializer,
    ReadingSerializer
)
from .models import (
    Label,
    Reading
)


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer


class ListLabelsView(TemplateView):
    template_name = 'app/list_labels.html'
