from django.contrib import admin

# Register your models here.
from .models import products

# Register your models here.
#モデルをadminに登録できる。
admin.site.register(products)
