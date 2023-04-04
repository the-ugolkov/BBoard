from django_filters import FilterSet, ModelChoiceFilter

from ads.models import Response, Ad


class ResponseFilter(FilterSet):
    ad__title = ModelChoiceFilter(
        field_name='ad__title',
        queryset=Ad.objects.all(),
        label='Объявление',
        empty_label='все'
    )

    class Meta:
        model = Response
        fields = {}
