from django.urls import path
from Hojicha import views

app_name = 'Hojicha'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('list/', views.product_list, name = 'list'),
    path('list2/', views.DetailView.as_view(), name = 'list2')

]

