from abc import ABC, abstractmethod

# -------- MENU --------
menu = {
    "Indian": {
        "paneer butter masala": 220, "dal makhani": 180, "chole bhature": 120,
        "rajma chawal": 130, "veg biryani": 160, "butter naan": 40,
        "roti": 20, "aloo paratha": 60
    },

    "Chinese": {
        "veg noodles": 140, "fried rice": 150, "manchurian": 170,
        "spring rolls": 120, "chilli paneer": 180, "hakka noodles": 160,
        "schezwan rice": 170
    },

    "Italian": {
        "pizza": 250, "pasta alfredo": 220, "pasta arrabbiata": 210,
        "lasagna": 280, "garlic bread": 120, "risotto": 260
    },

    "Fast Food": {
        "burger": 90, "fries": 70, "sandwich": 100,
        "wrap": 110, "hot dog": 120, "nachos": 130
    },

    "Beverages": {
        "coffee": 80, "tea": 30, "cold coffee": 120,
        "lemonade": 60, "soft drink": 50, "milkshake": 140,
        "green tea": 70
    },

    "Desserts": {
        "ice cream": 90, "gulab jamun": 60, "brownie": 120,
        "cake": 150, "rasgulla": 70, "kheer": 80,
        "halwa": 90
    }
}

# -------- VIEW MENU --------
def view_menu():
    print("\n========== MENU ==========")
    for category, items in menu.items():
        print(f"\n🔹 {category}")
        for item, price in items.items():
            print(f"   {item.capitalize()} : ₹{price}")
    print("==========================")

# -------- ORDER TYPE --------
def order_type():
    while True:
        print("\n1. Dine-in")
        print("2. Takeaway")

        choice = input("Select order type: ").strip()

        if choice == '1':
            return "Dine-in"
        elif choice == '2':
            return "Takeaway"
        else:
            print("❌ Invalid choice, try again")

# -------- PLACE ORDER --------
def place_order():
    total_cost = 0
    order_items = []

    while True:
        item = input("\nEnter item name (or 'done'): ").lower().strip()

        if item == "done":
            break

        found = False

        for category in menu:
            if item in menu[category]:
                while True:
                    try:
                        qty = int(input(f"Enter quantity of {item}: "))
                        if qty <= 0:
                            print("❌ Quantity must be positive")
                            continue
                        break
                    except ValueError:
                        print("❌ Enter a valid number")

                cost = menu[category][item] * qty
                total_cost += cost
                order_items.append((item, qty, cost))

                print(f"✅ Added {qty} x {item} = ₹{cost}")
                found = True
                break

        if not found:
            print("❌ Item not found in menu")

    return total_cost, order_items

# -------- DISCOUNT --------
def discount(total):
    if total > 1000:
        print("🎉 20% discount applied!")
        return total * 0.20
    elif total > 500:
        print("🎉 10% discount applied!")
        return total * 0.10
    return 0

# -------- GST --------
def gst(amount):
    gst_amt = amount * 0.05
    final = amount + gst_amt
    return final, gst_amt

# -------- BILL GENERATOR (Abstract) --------
class BillGenerator(ABC):
    @abstractmethod
    def generate(self, order_items, total, discount_amt, gst_amt, final_amt, order_type):
        """Generate the bill. Subclasses must implement this."""
        raise NotImplementedError()


class ConsoleBillGenerator(BillGenerator):
    def generate(self, order_items, total, discount_amt, gst_amt, final_amt, order_type):
        # Delegate to the existing `bill` function for printing
        bill(order_items, total, discount_amt, gst_amt, final_amt, order_type)

# -------- BILL --------
def bill(order_items, total, discount_amt, gst_amt, final_amt, order_type):
    print("\n========== BILL ==========")
    print(f"Order Type: {order_type}")

    for item, qty, cost in order_items:
        print(f"{item.capitalize()} x{qty} = ₹{cost}")

    print("--------------------------")
    print(f"Subtotal: ₹{total}")
    print(f"Discount: -₹{discount_amt:.2f}")
    print(f"GST (5%): +₹{gst_amt:.2f}")
    print("--------------------------")
    print(f"Final Amount: ₹{final_amt:.2f}")
    print("==========================")

# -------- DISPLAY --------
def display_menu():
    print("\n"+"="*30)
    print("🍽️  Welcome to Our Restaurant!  🍽️")
    print("="*30)
    
    for category, items in menu.items():
        print(f"\n🔹 {category.upper()}")
        for item, price in items.items():
            print(f"   {item.capitalize()} : ₹{price}")

# -------- MAIN --------
def main():
    print("🍽️  Welcome to Our Restaurant!")

    while True:
        ask = input("\nDo you want to place an order? (yes/no): ").lower().strip()

        if ask == "yes":
            break
        elif ask == "no":
            print("\n🙏 Thank you for visiting us!")
            return
        else:
            print("❌ Please type 'yes' or 'no'")

    o_type = order_type()

    display_menu()
    
    total, items = place_order()

    if total == 0:
        print("No order placed.")
    else:
        disc = discount(total)
        final_amt, gst_amt = gst(total - disc)

        # Use virtual bill generator
        generator = ConsoleBillGenerator()
        generator.generate(items, total, disc, gst_amt, final_amt, o_type)

    print("\n🙏 Thank you for visiting us!")

# Run program safely
if __name__ == "__main__":
    main()