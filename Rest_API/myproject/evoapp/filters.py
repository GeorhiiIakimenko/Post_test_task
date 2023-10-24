import django_filters
from myproject.evoapp.models import Post


class PostDateFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="created_at", lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name="created_at", lookup_expr='lte')

    class Meta:
        model = Post
        fields = ['start_date', 'end_date']
