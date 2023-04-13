from database import Product

try:
    p_name = input("Enter product name\n")
    p_qtty = input("Enter product quantity\n")
    p_price = input("Enter product price\n")
    Product.create(name=p_name, qtty=p_qtty, price=p_price)
    print("Product saved successfully")
except:
    print("Error occurred")

