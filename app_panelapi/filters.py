from .models import re_publish, stream
import django_filters


class Filter(django_filters.FilterSet):
    class Meta:
        model = re_publish
        fields = ['src_strm', ]

