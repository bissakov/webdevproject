from django.core.management.base import BaseCommand, CommandError
from store.models import Category,Product
import json

class Command(BaseCommand):
    def handle(self,*args,**options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        file_path = "C:/Users/bissa/Desktop/webdevproject/product_data/products.json"
        with open(file_path,'r',encoding='utf8') as f:
            data = json.load(f)
            for i in range(len(data)):
                if i % 5 == 0 or i == 0:
                    cat = Category()
                    cat.name = data[i]['category']
                    cat.save()
                prod = Product()
                prod.name = data[i]['name']
                prod.description = data[i]['description']
                prod.category = cat
                prod.price = data[i]['price']
                prod.likes = data[i]['likes']
                prod.save()
            
