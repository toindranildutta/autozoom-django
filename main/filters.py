import django_filters

from .models import Listing

class ListingFilter(django_filters.FilterSet):

    class Meta:
        model = Listing
        exclude = ('active',)
        fields = {'brand': ['exact'], 'transmission' : ['exact'], 'mileage' : ['lt'], 'model' : ['icontains'] }
        
