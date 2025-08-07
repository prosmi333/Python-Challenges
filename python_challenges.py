# How tall is big ben?

import turtle
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

# Hogwarts Sorting Hat Algorithm

gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

# Question 1
answer = input("Do you enjoy taking risks? (yes/no): ").lower()
if answer == "yes":
    gryffindor += 1
    slytherin += 1
else:
    hufflepuff += 1
    ravenclaw += 1

# Question 2
answer = input("Do you value loyalty? (yes/no): ").lower()
if answer == "yes":
    hufflepuff += 2
else:
    slytherin += 1

# Question 3
answer = input("Do you consider yourself clever? (yes/no): ").lower()
if answer == "yes":
    ravenclaw += 2
else:
    gryffindor += 1

# Question 4
answer = input(
    "Would you break the rules to achieve your goal? (yes/no): ").lower()
if answer == "yes":
    slytherin += 2
else:
    hufflepuff += 1

# Determine the winner
houses = {
    "Gryffindor": gryffindor,
    "Hufflepuff": hufflepuff,
    "Ravenclaw": ravenclaw,
    "Slytherin": slytherin
}

max_score = max(houses.values())

# Find all houses with the max score in case of a tie
top_houses = [house for house, score in houses.items() if score == max_score]

if len(top_houses) == 1:
    print("You belong to:", top_houses[0])
else:
    print("You could belong to one of these houses:", ", ".join(top_houses))


# Setup screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)


def drawWall(x, y, width, height, battlements, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()

    # Draw battlements
    pen.penup()
    pen.goto(x, y + height)
    pen.setheading(0)
    pen.pendown()
    for _ in range(battlements):
        pen.forward(width / battlements / 2)
        pen.left(90)
        pen.forward(10)
        pen.right(90)
        pen.forward(width / battlements / 2)
        pen.right(90)
        pen.forward(10)
        pen.left(90)


def drawTower(x, y, radius, height, color):
    pen.penup()
    pen.goto(x, y)
    pen.color(color)
    pen.begin_fill()
    pen.pendown()
    pen.circle(radius)
    pen.end_fill()
    pen.penup()
    pen.goto(x - radius, y)
    pen.pendown()
    pen.begin_fill()
    for _ in range(2):
        pen.forward(radius * 2)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()


def drawDoor(x, y, width, height, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()


# Draw Castle Elements
drawWall(-150, -100, 300, 100, 6, "grey")
drawTower(-180, 0, 30, 60, "darkgrey")
drawTower(150, 0, 30, 60, "darkgrey")
drawDoor(-25, -100, 50, 75, "brown")

pen.hideturtle()
screen.mainloop()


# Screen setup
screen = turtle.Screen()
screen.bgcolor("lightgreen")

# Draw start and finish lines


def draw_line(x_pos):
    line = turtle.Turtle()
    line.penup()
    line.goto(x_pos, 150)
    line.pendown()
    line.right(90)
    line.forward(300)
    line.hideturtle()


draw_line(-100)  # Start line
draw_line(100)   # Finish line

# Create turtles
colors = ["red", "blue", "yellow", "purple"]
racers = []

start_y = 100
for color in colors:
    racer = turtle.Turtle()
    racer.color(color)
    racer.shape("turtle")
    racer.penup()
    racer.goto(-100, start_y)
    start_y -= 50
    racers.append(racer)

# Race logic
winner = None
while not winner:
    for racer in racers:
        move = random.randint(1, 5)
        racer.forward(move)
        if racer.xcor() >= 100:
            winner = racer
            break

# Show winner
winner.write(f"{winner.color()[0].capitalize()} turtle wins!", font=(
    "Arial", 16, "bold"))

turtle.done()


# Screen setup
screen = turtle.Screen()
screen.bgcolor("skyblue")
myPen = turtle.Turtle()
myPen.speed(0)

# Draw crenellation pattern across the screen


def draw_crenellation(repeats, block_width=20, block_height=15):
    for _ in range(repeats):
        myPen.left(90)
        myPen.forward(block_height)
        myPen.right(90)
        myPen.forward(block_width)
        myPen.right(90)
        myPen.forward(block_height)
        myPen.left(90)
        myPen.forward(block_width)


# Position turtle at start
myPen.penup()
myPen.goto(-screen.window_width() // 2, 0)
myPen.pendown()
draw_crenellation(repeats=20)

myPen.hideturtle()
screen.mainloop()


def knightNameGenerator():
    firstnames = ["Lancelot", "Charles", "Henry",
                  "William", "James", "Richard", "Edward"]
    nicknames = ["Brave", "Horrific", "Courageous", "Terrific",
                 "Fair", "Conqueror", "Victorious", "Glorious", "Invincible"]
    firstname = random.choice(firstnames)
    nickname = random.choice(nicknames)
    return f"{firstname} the {nickname}"


def generateCoatOfArms():
    colours = ["Red", "Golden", "Blue", "Purple", "White", "Silver"]
    animals = ["Lion", "Dragon", "Unicorn", "Horse", "Tiger"]
    colour = random.choice(colours)
    animal = random.choice(animals)
    return f"{colour} {animal}"


def generateCoatOfArmsTwoColours():
    colours = ["Red", "Golden", "Blue", "Purple", "White", "Silver"]
    animals = ["Lion", "Dragon", "Unicorn", "Horse", "Tiger"]
    colour1 = random.choice(colours)
    colour2 = random.choice(colours)
    animal = random.choice(animals)
    if colour1 == colour2:
        return f"{colour1} {animal}"
    else:
        return f"{colour1} and {colour2} {animal}"


if __name__ == "__main__":
    player1_name = knightNameGenerator()
    player1_coa = generateCoatOfArmsTwoColours()
    print(f"Player 1: Your name is {player1_name}")
    print(f"Your coat of arms is a {player1_coa}")
