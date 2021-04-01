from django.db import models

# Create your models here.
class products(models.Model):
    product_name = models.CharField(verbose_name="商品名", null=False, max_length=30)
    price = models.CharField(verbose_name="価格",max_length = 15)
    media_data = models.ImageField(verbose_name ="画像",null = False, upload_to = 'document',)
    URL = models.URLField(verbose_name="URL", null=True, max_length=400)

    def __str__(self):
        return self.productname_name\
