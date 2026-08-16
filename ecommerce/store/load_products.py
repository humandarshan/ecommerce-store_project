import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from store.models import Product

PRODUCTS = [
    {"name": "Laptop", "price": 50000, "category": "electronics",
     "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=800&q=80"},
    {"name": "Mobile Phone", "price": 20000, "category": "electronics",
     "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=800&q=80"},
    {"name": "Headphones", "price": 2000, "category": "electronics",
     "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=600&q=80"},
    {"name": "Smart Watch", "price": 5000, "category": "electronics",
     "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=600&q=80"},
    {"name": "Bluetooth Speaker", "price": 3500, "category": "electronics",
     "image": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?auto=format&fit=crop&w=600&q=80"},
    {"name": "Men's T-Shirt", "price": 799, "category": "fashion",
     "image":"https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=600&q=80"},
    {"name": "Men's Jeans", "price": 1499, "category": "fashion",
     "image":"https://images.unsplash.com/photo-1542272604-787c3835535d?auto=format&fit=crop&w=600&q=80"},
    {"name": "Women's Dress", "price": 1999, "category": "fashion",
     "image":"https://images.unsplash.com/photo-1595777457583-95e059d581b8?auto=format&fit=crop&w=600&q=80"},
    {"name": "Jacket", "price": 2499, "category": "fashion",
     "image":"https://images.unsplash.com/photo-1551028719-00167b16eac5?auto=format&fit=crop&w=600&q=80"},
    {"name": "Sports Shoes", "price": 2999, "category": "fashion",
     "image":"https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=600&q=80"},
    {"name": "Dior Sauvage", "price": 8999, "category": "perfumes",
     "image":"https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=600&q=80"},
    {"name": "Chanel No. 5", "price": 12999, "category": "perfumes",
     "image":"https://images.unsplash.com/photo-1541643600914-78b084683601?auto=format&fit=crop&w=600&q=80"},
    {"name": "Gucci Bloom", "price": 9499, "category": "perfumes",
     "image":"https://images.unsplash.com/photo-1563170351-be82bc888aa4?auto=format&fit=crop&w=600&q=80"},
    {"name": "Versace Eros", "price": 7999, "category": "perfumes",
     "image":"https://images.unsplash.com/photo-1587017539504-67cfbddac569?auto=format&fit=crop&w=600&q=80"},
    {"name": "Calvin Klein CK One", "price": 3999, "category": "perfumes",
     "image":"https://images.unsplash.com/photo-1523293188086-b6e7a0f6d9d0?auto=format&fit=crop&w=600&q=80"},
    {"name": "Sofa Cushion", "price": 599, "category": "home",
     "image":"https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?auto=format&fit=crop&w=600&q=80"},
    {"name": "Decorative Table Lamp", "price": 1299, "category": "home",
     "image":"https://images.unsplash.com/photo-1507473885765-e6ed057f782c?auto=format&fit=crop&w=600&q=80"},
    {"name": "Wall Clock", "price": 899, "category": "home",
     "image":"https://images.unsplash.com/photo-1563861826100-9cb868fdbe1c?auto=format&fit=crop&w=600&q=80"},
    {"name": "Indoor Plant Pot", "price": 499, "category": "home",
     "image":"https://images.unsplash.com/photo-1485955900006-10f4d324d411?auto=format&fit=crop&w=600&q=80"},
    {"name": "Bedsheet Set", "price": 1599, "category": "home",
     "image":"https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?auto=format&fit=crop&w=600&q=80"},
    {"name": "Coffee Mug Set", "price": 499, "category": "home",
     "image":"https://images.unsplash.com/photo-1514228742587-6b1558fcf93a?auto=format&fit=crop&w=600&q=80"},
    {"name": "Scented Candles", "price": 699, "category": "home",
     "image":"https://images.unsplash.com/photo-1602874801006-e26f0c4d4b7c?auto=format&fit=crop&w=600&q=80"},
    {"name": "Door Mat", "price": 399, "category": "home",
     "image":"https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&w=600&q=80"},
]

created_count = 0
for item in PRODUCTS:
    obj, created = Product.objects.get_or_create(
        name=item["name"],
        defaults={
            "price": item["price"],
            "category": item["category"],
            "image": item.get("image", ""),
        },
    )
    if created:
        created_count += 1

print(f"Done. Created {created_count} new products.")