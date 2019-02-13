from .models import re_publish, stream, server_id
import django_filters


class Filter(django_filters.FilterSet):
    src_strm = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = re_publish
        fields = ['src_strm']


class Filter1(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = stream
        fields = ['name']

