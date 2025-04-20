import django_filters

from users.models import UserProfile


class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(
        field_name="user__username", lookup_expr="icontains"
    )
    name = django_filters.CharFilter(field_name="user__name", lookup_expr="icontains")

    class Meta:
        model = UserProfile
        fields = "__all__"
