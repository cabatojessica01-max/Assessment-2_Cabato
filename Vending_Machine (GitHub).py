items = [
    # ————————— Sour Patch —————————
    {"code": "SP1", "name": "Sour Patch Kids - Original", "price": 6.00, "stock": 10, "type": "snack"},
    {"code": "SP2", "name": "Sour Patch Watermelon", "price": 6.50, "stock": 10, "type": "snack"},
    {"code": "SP3", "name": "Sour Patch Extreme", "price": 7.00, "stock": 10, "type": "snack"},
    {"code": "SP4", "name": "Sour Patch Blue Raspberry", "price": 6.50, "stock": 10, "type": "snack"},
    {"code": "SP5", "name": "Sour Patch Berries", "price": 6.75, "stock": 10, "type": "snack"},
    {"code": "SP6", "name": "Sour Patch Tropical", "price": 7.25, "stock": 10, "type": "snack"},
    {"code": "SP7", "name": "Sour Patch Fire", "price": 7.50, "stock": 10, "type": "snack"},
    {"code": "SP8", "name": "Sour Patch Strawberry", "price": 6.25, "stock": 10, "type": "snack"},
    {"code": "SP9", "name": "Sour Patch Peach", "price": 6.50, "stock": 10, "type": "snack"},
    {"code": "SP10", "name": "Sour Patch Grape", "price": 7.00, "stock": 10, "type": "snack"},

    # ————————— Chocolates —————————
    {"code": "CH1", "name": "Twix", "price": 4.00, "stock": 10, "type": "chocolate"},
    {"code": "CH2", "name": "KitKat", "price": 3.50, "stock": 10, "type": "chocolate"},
    {"code": "CH3", "name": "Snickers", "price": 4.25, "stock": 10, "type": "chocolate"},
    {"code": "CH4", "name": "Galaxy", "price": 5.00, "stock": 10, "type": "chocolate"},
    {"code": "CH5", "name": "Bounty", "price": 3.75, "stock": 10, "type": "chocolate"},
    {"code": "CH6", "name": "M&M's", "price": 4.50, "stock": 10, "type": "chocolate"},
    {"code": "CH7", "name": "Reese's Cups", "price": 5.25, "stock": 10, "type": "chocolate"},
    {"code": "CH8", "name": "Milky Way", "price": 3.90, "stock": 10, "type": "chocolate"},
    {"code": "CH9", "name": "Ferrero Rocher Mini", "price": 6.50, "stock": 10, "type": "chocolate"},
    {"code": "CH10", "name": "Toblerone Mini", "price": 5.75, "stock": 10, "type": "chocolate"},

    # ————————— Drinks —————————
    {"code": "D1", "name": "Coca-Cola Can", "price": 4.50, "stock": 10, "type": "drink"},
    {"code": "D2", "name": "Pepsi Can", "price": 4.25, "stock": 10, "type": "drink"},
    {"code": "D3", "name": "Water Bottle", "price": 2.00, "stock": 10, "type": "drink"},
    {"code": "D4", "name": "Calamansi Juice", "price": 5.50, "stock": 10, "type": "drink"},
    {"code": "D5", "name": "Ice Tea Lemon", "price": 5.00, "stock": 10, "type": "drink"},
]

#  ————————— FUNCTIONS  —————————

def display_welcome():
    print("\n———————————————————————————————————————")
    print("   WELCOME TO THE ULTIMATE VENDING MACHINE")
    print("———————————————————————————————————————")
    print("You can select snacks, chocolates, and drinks.")
    print("Type the product code to add items to your cart.")
    print("Type 'exit' when you are done selecting.\n")


def display_menu():
    print("\n————————— AVAILABLE PRODUCTS —————————")
    for item in items:
        print(f"{item['code']} | {item['name']:35} | {item['price']} SAR | Stock: {item['stock']}")
    print("———————————————————————————————————————")


def find_item(code):
    for item in items:
        if item["code"] == code:
            return item
    return None


def suggest_drink():
    available_drinks = [d for d in items if d["type"] == "drink" and d["stock"] > 0]
    if available_drinks:
        drink = available_drinks[0]
        print(f"💡 Suggestion: How about a drink? Try {drink['name']} for {drink['price']} SAR.")


def vending_machine():
    cart = []
    total_balance = 0.0
    display_welcome()  # It will show welcome message at the start

    # ————————— ITEM SELECTION —————————
    while True:
        display_menu()
        choice = input("\nEnter product code (or 'exit' to finish): ").upper()

        if choice == "EXIT":
            break

        product = find_item(choice)

        if product is None:
            print("❌ Invalid product code.")
            continue

        if product["stock"] <= 0:
            print(f"❌ {product['name']} is out of stock.")
            continue

        cart.append(product)
        total_balance += product["price"]
        product["stock"] -= 1

        print(f"\n🛒 {product['name']} added to cart. Current total: {total_balance:.2f} SAR")

        # Suggest drink if a snack or chocolate is added
        if product["type"] in ["snack", "chocolate"]:
            suggest_drink()

        more = input("Do you want to add another item? (yes/no): ").lower()
        if more != "yes":
            break

    if not cart:
        print("\nNo items selected. Thank you!")
        return

    # ————————— SUMMARY —————————
    print("\n—————— PURCHASE SUMMARY ——————")
    for item in cart:
        print(f"- {item['name']} : {item['price']} SAR")
    print(f"TOTAL AMOUNT: {total_balance:.2f} SAR")

    # ————————— PAYMENT METHOD —————————
    while True:
        payment_method = input("\nPay with CASH or CARD? ").upper()
        if payment_method in ["CASH", "CARD"]:
            break
        print("❌ Please enter CASH or CARD only.")

    # ————————— CASH PAYMENT WITH MULTIPLE INSERTS —————————
    if payment_method == "CASH":
        inserted_money = 0.0
        while inserted_money < total_balance:
            try:
                cash = float(input(f"Insert cash (Remaining: {total_balance - inserted_money:.2f} SAR): "))
                inserted_money += cash
                if inserted_money < total_balance:
                    print(f"💰 Total inserted so far: {inserted_money:.2f} SAR")
            except ValueError:
                print("❌ Enter a valid number.")

        change = inserted_money - total_balance
        print(f"✔ Payment complete! 💰 Change returned: {change:.2f} SAR")

    # ————————— CARD PAYMENT —————————
    else:
        print("💳 Processing card payment...")
        print("✔ Payment successful.")

    print("\n🎉 Transaction complete. Thank you for using the vending machine!")


# ———————————————— RUN PROGRAM ————————————————
vending_machine()