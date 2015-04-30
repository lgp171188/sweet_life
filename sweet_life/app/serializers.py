from rest_framework import serializers

from .models import (
    Label,
    Reading
)


class LabelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Label
        fields = ('id', 'url', 'name', 'description')


class ReadingSerializer(serializers.HyperlinkedModelSerializer):
    label_name = serializers.SerializerMethodField('label_name')

    def label_name(self, reading):
        return reading.label_name()

    class Meta:
        model = Reading
        fields = ('id', 'url', 'when', 'value', 'label', 'label_name')
