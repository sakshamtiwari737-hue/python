# Online Food Ordering System (PS 44)
**Name**: Saksham Tiwari

**Class**: B.tech CSE Core,1st semester

**ERP**: RU-26-02695

**Section**: K

A simple console-based food ordering program written in Python 3.
The customer adds items to a cart, applies a coupon, and checks out to get a final bill.

## What is in this repository

| File | Description |
|------|-------------|
| `food_ordering.py` | Main Python program (run this file) |
| `README.md` | This file - explains the repository |
| `summary.md` | Difficulties faced during the project and test case screenshots |
| `screenshots/` | Screenshots of the 4 test cases |

## Features

- Menu stored in a dictionary, cart stored in a list
- Add items and remove items from the cart
- View the cart and the cart subtotal
- Apply a coupon code (`SAVE10` gives 10% off the subtotal)
- Bill calculation: subtotal, discount, GST (5%), delivery charge and total
- Delivery is Rs.40, and it is free if the subtotal is Rs.300 or more
- Validation of item name, quantity and coupon code

## Menu

| Item | Price |
|------|-------|
| Burger | Rs.120 |
| Pizza | Rs.250 |
| Fries | Rs.80 |
| Coke | Rs.40 |

## How to run

1. Install Python 3.
2. Open a terminal in the project folder.
3. Run:

    python food_ordering.py

4. Choose options from the menu (1 to 6) and follow the prompts.

## Bill formula

    discount = subtotal * 10%   (only if SAVE10 is applied)
    gst      = (subtotal - discount) * 5%
    delivery = 0 if subtotal >= 300 else 40
    total    = subtotal - discount + gst + delivery

## Concepts used

Lists, Dictionaries, Functions, Loops, Input validation, Billing calculation
