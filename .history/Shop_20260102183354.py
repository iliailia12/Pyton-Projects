# პროდუქტის ინფორმაცია (სახელი, ფასი და რაოდენობა)
products = [
    {"name": "T-shirt", "price": 25, "quantity": 50},
    {"name": "Jeans", "price": 50, "quantity": 30},
    {"name": "Cap", "price": 15, "quantity": 100}
]

# პროდუქტის მახასიათებლების ნახვა
def display_products():
    if not products:
        print("Store is empty.")
    for product in products:
        print(f"{product['name']} - {product['price']} GEL - {product['quantity']} in stock")

# პროდუქტის გაყიდვა
def sell_product(product_name, quantity_sold):
    for product in products:
        if product["name"] == product_name:
            if product["quantity"] >= quantity_sold:
                product["quantity"] -= quantity_sold
                print(f"{quantity_sold} {product_name}(s) sold!")
                return
            else:
                print(f"Not enough {product_name} in stock!")
                return
    print(f"Product {product_name} not found in the store.")

# ახალი პროდუქტის დამატება
def add_product(name, price, quantity):
    products.append({"name": name, "price": price, "quantity": quantity})
    print(f"{name} added to the store.")

# მომხმარებლისგან მოქმედებების მიღება
display_products()  # პირველად ვხედავთ ყველა პროდუქტის მონაცემებს

sell_product("T-shirt", 5)  # გაყიდვა 5 T-shirt
sell_product("Jeans", 3)  # გაყიდვა 3 Jeans

# პროდუქტის დამატება
add_product("Socks", 5, 200)  # ახალი პროდუქტი Socks

display_products()  # ბოლოს ყველა პროდუქტის გადახედვა
