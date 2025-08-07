# How tall is big ben?

import random


def estimate_the_height(l, h, L):
    estimated_height = round((h * L) / l)
    print(f"The estimate height of this building is {estimated_height} meters")


estimate_the_height(1.74, 2.51, 66.55)

# Animal name generator


def left(s, n):
    return s[:n]


def right(s, n):
    return s[-n:] if n <= len(s) else s


def substr(s, start, length):
    return s[start:start+length]


def random_fragment(name):
    length = len(name)
    if length == 0:
        return ""
    choice = random.choice(['left', 'right', 'substr'])
    if choice == 'left':
        n = random.randint(1, length)
        return left(name, n)
    elif choice == 'right':
        n = random.randint(1, length)
        return right(name, n)
    else:
        if length == 1:
            return name
        start = random.randint(0, length - 1)
        max_len = length - start
        length_sub = random.randint(1, max_len)
        return substr(name, start, length_sub)


def make_name(names):
    fragments = [random_fragment(n) for n in names]
    return "".join(fragments).capitalize()


def explorer_name_generator():
    print("Welcome to the Explorer’s Name Generator!")
    raw = input(
        "Enter at least two existing animal names, separated by commas: ")
    names = [n.strip() for n in raw.split(',') if n.strip()]
    if len(names) < 2:
        print("Please enter at least two names.")
        return
    while True:
        new = make_name(names)
        print("How about:", new)
        ok = input("Do you like this name? (y/n): ").strip().lower()
        if ok == 'y':
            print("Great! Your new species is named:", new)
            break
        else:
            print("Let's try again...")


if __name__ == "__main__":
    explorer_name_generator()

# Egg Farmer


def pack_eggs(total_eggs):
    cartons12 = total_eggs // 12
    rem = total_eggs % 12

    cartons6 = 0
    if rem >= 6:
        cartons6 = 1
        rem -= 6

    return cartons12, cartons6, rem


def main():
    total = int(input("How many eggs did you pick up today? "))
    c12, c6, leftover = pack_eggs(total)

    print(f"You will need {c12} carton{'s' if c12 != 1 else ''} of 12.")
    if c6:
        print("You will need 1 carton of 6.")
    print(
        f"You will have {leftover} egg{'s' if leftover != 1 else ''} for breakfast!")


if __name__ == "__main__":
    main()

# AI bot
for i in range(0, 101):
    print("I will listen to my teacher and complete my work on time.")

# Coffee shop
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+              Welcome          +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees:")
print(" > Espresso")
print(" > Americano")
print(" > Latte")
print(" > Cappuccino")
print(" > Macchiato")
print(" > Mocha")
print(" > Flat White")
print("----------------------------")

coffee_prices = {
    "Espresso": 2.50,
    "Americano": 3.00,
    "Latte": 2.50,
    "Cappuccino": 3.20,
    "Macchiato": 2.80,
    "Mocha": 3.30,
    "Flat White": 2.90
}

size_prices = {
    "small": 0.00,
    "medium": 0.50,
    "large": 1.00
}

total_price = 0
ordering = True

while ordering:
    coffee = input("What type of coffee would you like? ").title()
    if coffee not in coffee_prices:
        print("Sorry, we don't serve that coffee.")
        continue

    size = input("What size? (small / medium / large): ").lower()
    if size not in size_prices:
        print("Invalid size. Defaulting to small.")
        size = "small"

    price = coffee_prices[coffee] + size_prices[size]

    if coffee == "Latte":
        syrup = input(
            "Would you like flavored syrup for £0.50? (yes/no): ").lower()
        if syrup == "yes":
            price += 0.50

    print(f"{size.title()} {coffee}: £{price:.2f}")
    total_price += price

    more = input("Would you like to order another coffee? (yes/no): ").lower()
    if more != "yes":
        ordering = False


is_student = input("Are you a student? (yes/no): ").lower()
tax = 0
if is_student != "yes":
    tax = total_price * 0.0625

final_total = total_price + tax

print("----------------------------")
print(f"Subtotal: £{total_price:.2f}")
print(f"Tax: £{tax:.2f}")
print(f"Total Cost: £{final_total:.2f}")

# Ice Cream


def get_container():
    while True:
        c = input("Container (Cup or Cone): ").strip().lower()
        if c in ("cup", "cone"):
            return c
        print("Please enter 'Cup' or 'Cone'.")


def get_scoops():
    while True:
        try:
            n = int(input("Number of scoops (1‑4): ").strip())
            if 1 <= n <= 4:
                return n
        except ValueError:
            pass
        print("Please enter a number between 1 and 4.")


def get_yes_no(prompt):
    while True:
        ans = input(prompt + " (Yes or No): ").strip().lower()
        if ans in ("yes", "no"):
            return ans == "yes"
        print("Please enter Yes or No.")


def calculate_price(container, scoops, flake, sprinkles, coulis):
    # Base prices
    if container == "cone":
        base = 1.00
    else:  # cup
        base = 1.50
    scoop_price = {1: 1.00, 2: 2.00, 3: 2.50, 4: 3.00}
    total = base + scoop_price[scoops]
    if flake:
        total += 0.60
    if sprinkles:
        total += 0.30
    if coulis:
        total += 0.80
    return total


def main():
    print("Welcome to the Ice Cream Price Calculator!")
    container = get_container()
    scoops = get_scoops()
    flake = get_yes_no("Add flake")
    sprinkles = get_yes_no("Add chocolate sprinkles")
    coulis = get_yes_no("Add strawberry coulis")

    price = calculate_price(container, scoops, flake, sprinkles, coulis)
    print(f"Ice Cream Price: £{price:.2f}")


if __name__ == "__main__":
    main()


# Investment

def get_amount(prompt):
    while True:
        try:
            val = float(input(prompt).strip())
            if val < 0:
                print("Please enter a non‑negative number.")
                continue
            return val
        except ValueError:
            print("Please enter a valid number (e.g. 450 or 1250.50).")


def main():
    print("Return on Investment Calculator")
    total_costs = get_amount("Enter total costs/investment (£): ")
    total_sales = get_amount("Enter total sales/revenue (£): ")

    profit = total_sales - total_costs
    # ROI as a percentage
    if total_costs > 0:
        roi = (profit / total_costs) * 100
    else:
        roi = float('inf')  # Avoid divide by zero

    # Profit or loss message
    if profit > 0:
        status = "profit"
    elif profit < 0:
        status = "loss"
    else:
        status = "no profit or loss"

    print(f"\nProfit (or loss): £{profit:.2f} ({status})")
    if total_costs > 0:
        print(f"Return on Investment (ROI): {roi:.0f}%")
    else:
        print("ROI: undefined (costs were zero or zero investment)")


if __name__ == "__main__":
    main()
