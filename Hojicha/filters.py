import django_filters
from .models import products
 

class ProductsFilter(django_filters.FilterSet):

    class Meta:
        model = products
        fields = {
            'product_name':{'icontains'} ,
            'price':{'icontains'}
          
            }