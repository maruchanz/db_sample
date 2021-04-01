import django_tables2 as tables
from .forms import ProductsForm
from .models import products

class ItemTable(tables.Table):
    class Meta:
        model = products
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('product_name', 'price','media_data','URL')

