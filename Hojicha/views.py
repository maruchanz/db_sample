from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .forms import ProductsForm
from django.template.response import TemplateResponse
from django_tables2 import SingleTableView
from .tables import ItemTable
from .models import products
from .filters import ProductsFilter

# Create your views here.
def index(request):
      return render(request, 'index.html')


def product_list(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST,request.FILES)
      #   is_valid = form.is_valid()    
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()         
        
        return TemplateResponse(request, 'index.html',
                                {'form': form})
    else:            
        form = ProductsForm()
    

    return TemplateResponse(request, 'list.html',
                                {'form':form})

class DetailView(SingleTableView):
    table_class = ItemTable
    # nameでの表記可能？
    template_name = 'list2.html'
    model = products
  
    def get_queryset(self):
        # data=questionnaire.objects.order_by("id")
        # print(data)
        return products.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        # print(self.request.GET)
        # print(self.get.queryset())
        context['filter'] = ProductsFilter(self.request.GET, queryset = products.objects.all())
        return context

