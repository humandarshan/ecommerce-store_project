import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from store.models import Product

for pid in range(6, 24):
    try:
        product = Product.objects.get(id=pid)
        product.image = f"/static/store/products/{pid}.png"
        product.save()
        print(f"Updated {product.name}")
    except Product.DoesNotExist:
        print(f"Product id {pid} not found, skipping")

print("Done.")