"""Online Food Ordering System (PS 44)
Console app: add items to a cart, apply a coupon, checkout with a bill.
"""

MENU = {"Burger": 120, "Pizza": 250, "Fries": 80, "Coke": 40}
COUPONS = {"SAVE10": 0.10}   # code -> discount rate
GST_RATE = 0.05
DELIVERY_CHARGE = 40
FREE_DELIVERY_AT = 300

cart = []             # list of {"item": str, "qty": int}
applied_coupon = None


def menu_text():
    return ", ".join(MENU)


def find_item(name):
    """Case-insensitive lookup; returns the canonical menu name or None."""
    for item in MENU:
        if item.lower() == name.strip().lower():
            return item
    return None


def add_item(name, qty):
    item = find_item(name)
    if item is None:
        print(f"Item not available. Menu: {menu_text()}")
        return False
    if not isinstance(qty, int) or qty <= 0:
        print("Invalid quantity. Enter a whole number greater than 0.")
        return False
    for line in cart:
        if line["item"] == item:
            line["qty"] += qty
            break
    else:
        cart.append({"item": item, "qty": qty})
    print(f"{item} x{qty} added to cart | Cart subtotal: {subtotal()}")
    return True


def remove_item(name):
    item = find_item(name)
    for line in cart:
        if line["item"] == item:
            cart.remove(line)
            print(f"{item} removed from cart | Cart subtotal: {subtotal()}")
            return True
    print("Item not in cart.")
    return False


def subtotal():
    return sum(MENU[l["item"]] * l["qty"] for l in cart)


def apply_coupon(code):
    global applied_coupon
    code = code.strip().upper()
    if code not in COUPONS:
        print("Invalid coupon code. Only SAVE10 is accepted.")
        return False
    applied_coupon = code
    print("Coupon SAVE10 applied: 10% off the subtotal.")
    return True


def calculate_bill():
    sub = subtotal()
    discount = sub * COUPONS[applied_coupon] if applied_coupon else 0.0
    gst = (sub - discount) * GST_RATE
    delivery = 0 if sub >= FREE_DELIVERY_AT else DELIVERY_CHARGE
    total = sub - discount + gst + delivery
    return sub, discount, gst, delivery, total


def checkout():
    if not cart:
        print("Cart is empty. Add items before checkout.")
        return False
    sub, discount, gst, delivery, total = calculate_bill()
    pct = " (10%)" if applied_coupon else ""
    d_text = "0 (free)" if delivery == 0 else str(delivery)
    print(f"Subtotal: {sub} | Discount{pct}: {discount:.2f}")
    print(f"GST (5%): {gst:.2f} | Delivery: {d_text}")
    print(f"Total: {total:.2f}")
    return True


def view_cart():
    if not cart:
        print("Cart is empty.")
        return
    for l in cart:
        print(f"  {l['item']} x{l['qty']} = {MENU[l['item']] * l['qty']}")
    print(f"  Cart subtotal: {subtotal()}")


def main():
    print("=== Online Food Ordering System ===")
    print("Menu: " + ", ".join(f"{k} Rs.{v}" for k, v in MENU.items()))
    while True:
        print("\n1.Add item  2.Remove item  3.View cart  4.Apply coupon  5.Checkout  6.Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            name = input("Add to cart: ")
            try:
                qty = int(input("Quantity: "))
            except ValueError:
                qty = 0
            add_item(name, qty)
        elif choice == "2":
            remove_item(input("Remove item: "))
        elif choice == "3":
            view_cart()
        elif choice == "4":
            apply_coupon(input("Coupon: "))
        elif choice == "5":
            if checkout():
                break
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()