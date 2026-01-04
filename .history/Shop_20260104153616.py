
# ინგლისურ კომენტარებს მერე დავუწერ


# მომხმარებლის ბიუჯეტი შემოიტანს  და სტრინგი გადაკეთდება ფლოატზე
user_budget = float(input("Enter your budget: $"))

# დახმარების მესიჯი მგონი პატარა
help_message = """
Welcome to Ilias Store! 🎉
Ready to find something special? We’re happy to help you get started.

Type "help" at any time to see this message.

Our store has the following sections:
electronics_sect, clothing_sect, shoes_sect, kitchen_sect, skincare_sect,
home_decor_sect, bathroom_sect, sports_fitness_sect, accessories_sect,
kids_items_sect, toys_sect, stationery_sect, cleaning_products_sect,
office_supplies_sect, bags_backpacks_sect, lighting_sect,
furniture_small_sect, pet_supplies_sect, garden_items_sect,
automotive_accessories_sect

How sections work:
- When you type a section name, products will be shown based on your budget.
- Only items with a price equal to or lower than your budget will appear.

Example:
If your budget is $100 and you type "electronics_sect",
you will see products that cost $100 or less (for example $60, $50, etc.).

Viewing all products in a section:
- Type: whole_sect_of_electronics_sect
(or simply: whole section of electronics)

Ordering products:
- Type: i want to order product_name_quantity
Example:
i want to order electronics_sect_keyboard_2
(This means you are ordering 2 keyboards.)

Other notes:
- You can view the whole section by typing: view_whole_sect
- The system accepts some invalid input errors and will still try to help you.

Enjoy shopping at Ilias Store! 🛒
"""

# ეს პროგრამა აჩვენებს პროდუქტებს ბიუჯეტის მიხედვით
def view_section(user_input):
    user_input = user_input.strip().lower() #strip მეთოდიი
    section_found = False  # იმის დასადგენად, რომ სექცია მყარი ყოფილა

    for section_name in all_sections:
        if user_input == section_name.lower():  # რეგისტრის შეუმჩნეველი შედარება
            section = all_sections[section_name]
            print(f"Displaying items from {section_name} within your budget:")
            found_item = False  # Check if any product matches the budget
            for product in section.values():
                if product['price'] <= user_budget:
                    print(f"{product['name']} - ${product['price']} (Stock: {product['stock']})")
                    found_item = True
            if not found_item:
                print("No items in this section match your budget.")
                print("You may want to try a different section or check for lower-priced items.")
            section_found = True  # გამოგზავნით სექციას
            break

    if not section_found:
        print("Invalid section! Please check the available section names.")

# შეკვეთის პროცესის დამუშავება
def process_order(order_input):
    global user_budget  # აქვე გამოვიყენებთ "global", რადგან ცვლადი ცვლილებას განიცდის
    try:
        order_input = order_input.lower().strip()  # რეგისტრის დამუშავება
        section_name, product_name, quantity = order_input.split("_")  # "_" ის მიხედვით გაყოფა
        quantity = int(quantity)

        # გადავამოწმებთ სექციას და პროდუქტს
        if section_name in all_sections and product_name in all_sections[section_name]:
            product = all_sections[section_name][product_name]
            if product['stock'] >= quantity:
                total_price = product['price'] * quantity
                if total_price <= user_budget:
                    print(f"Order placed: {quantity}x {product['name']} - ${total_price}")
                    product['stock'] -= quantity
                    user_budget -= total_price  # ასევე განახლდება ბიუჯეტი
                else:
                    print("Not enough budget!")
            else:
                print("Not enough stock!")
        else:
            print("Invalid section or product!")
    except ValueError:
        print("Invalid input format. Example: i want to order car_seat_cover_2")

# ძირითადი ლუპი
while True:
    user_input = input("Enter a command or section (or type 'exit' to quit): ").strip()

    if user_input == "help":
        print(help_message)  # აქ გამოიტანს მთლიანად `help_message`
    elif user_input == "exit":
        break
    elif user_input.startswith("i want to order"):
        process_order(user_input[16:].strip())  # ამოჭრავს "i want to order " ნაწილს
    elif user_input.startswith("view_whole_sect"):
        view_section(user_input)  # მთელი სექციის ნახვა
    else:
        view_section(user_input)  # ნებისმიერი სექციის ნახვა
