from rest_framework import serializers
from django.conf import settings
from .models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Resource
        fields = ('source', 'short_link', 'created', 'session')
        extra_kwargs = {
            'session': {'write_only': True, 'required': False},
            'short_link': {'required': False, 'min_length': settings.LENGTH_SHORT_FORM},
        }

    def to_internal_value(self, data):
        # clear data similar False stuff, is relevant for empty custom short_link
        _data = dict((key, val) for key, val in data.items() if val)

        return super().to_internal_value(_data)

    def validate(self, data):
        short_name = data.get('short_link')

        errors = dict()
        if Resource.objects.filter(short_link=short_name).exists():
            errors['short_link'] = ['This short is exists']

        if errors:
            raise serializers.ValidationError(errors)

        return super().validate(data)
