import django_filters


class PostFilter(django_filters.FilterSet):
    author_name = django_filters.CharFilter(
        field_name="user__name", lookup_expr="icontains"
    )
    author_username = django_filters.CharFilter(
        field_name="user__username", lookup_expr="icontains"
    )

    class Meta: ...
