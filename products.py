from database import Product

products = Product.select()
for product in products:
    print(product.name, product.qtty, product.price)
