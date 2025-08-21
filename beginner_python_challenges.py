import string
import sys
import time
import random
# How tall is big ben?


def estimate_the_height(l, h, L):
    estimated_height = round((h * L) / l)
    print(f"The estimate height of this building is {estimated_height} meters")


estimate_the_height(1.74, 2.51, 66.55)

# Animal name generator


def animal_name_generator():

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


def coffee_shop():

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

        more = input(
            "Would you like to order another coffee? (yes/no): ").lower()
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


def ice_cream_function():

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
        else:
            # cup
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
        roi = float('inf')

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


def Hogwarts_Sorting_Hat_Algorithm():

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
    top_houses = [house for house,
                  score in houses.items() if score == max_score]

    if len(top_houses) == 1:
        print("You belong to:", top_houses[0])
    else:
        print("You could belong to one of these houses:", ", ".join(top_houses))


# Knight

def Knight_Generator():

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

# World in 2050


message = "Rovvy, Gybvn!"

for i in range(26):
    decodedMessage = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                decodedMessage += chr((ord(char) - ord('a') - i) %
                                      26 + ord('a'))
            else:
                decodedMessage += chr((ord(char) - ord('A') - i) %
                                      26 + ord('A'))
        else:
            decodedMessage += char
    print(f"Caesar Cipher {i}: {decodedMessage}")

# Fish and Chips

a = "chips"
b = "fish"

c = a
a = b
b = c

print(a + " and " + b)

# Math Fraction Hack Algorithm


def math_fraction_algoritm():
    # First fraction
    a = int(input("Enter the numerator of the first fraction:"))
    b = int(input("Enter the denominator of the first fraction:"))
    print("First Fraction: " + str(a) + "/" + str(b))
    # Second fraction
    c = int(input("Enter the numerator of the second fraction:"))
    d = int(input("Enter the denominator of the second fraction:"))
    print("Second Fraction: " + str(c) + "/" + str(d))
    # Calculation
    first_cross_product = a * d
    second_cross_product = b * c
    # Comparing values
    if first_cross_product < second_cross_product:
        print(
            f"the numerator of the first fraction multiplied by the denominator of the second fraction({first_cross_product}) is smaller than the numerator of the second fraction multiplied by the denominator of the first fraction({second_cross_product})")
    elif second_cross_product < first_cross_product:
        print(
            f"the numerator of the first fraction multiplied by the denominator of the second fraction({first_cross_product}) is greater than the numerator of the second fraction multiplied by the denominator of the first fraction({second_cross_product})")
    else:
        print("The results from multiplying both fractions are the same.")
    # Printing the output
    print(
        f"The outcome of the butterfly method is {first_cross_product}, {second_cross_product}")


math_fraction_algoritm()

# Dice game


def dice_game():
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("+                               +")
    print("+         Welcome to the        +")
    print("+           Dice Game :3        +")
    print("+                               +")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

    player_1 = input("Player 1, Enter your name: ")
    counter1 = 0
    while True:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        counter1 += 1
        print(f"{player_1} rolled: {die1} and {die2}")
        if die1 == 6 and die2 == 6:
            break
    print(f"{player_1} got double sixes in {counter1} rolls.\n")

    player_2 = input("Player 2, Enter your name: ")
    counter2 = 0
    while True:
        die3 = random.randint(1, 6)
        die4 = random.randint(1, 6)
        counter2 += 1
        print(f"{player_2} rolled: {die3} and {die4}")
        if die3 == 6 and die4 == 6:
            break
    print(f"{player_2} got double sixes in {counter2} rolls.\n")

    if counter1 < counter2:
        print(f"{player_1} wins by {counter2 - counter1} fewer rolls! Congrats🎉")
    elif counter2 < counter1:
        print(f"{player_2} wins by {counter1 - counter2} fewer rolls! Congrats🎉")
    else:
        print("It's a tie! Both players rolled double sixes in the same number of tries! Congrats🎉")


dice_game()

# Typing Text Effect


def typing_print(text, delay=0.05):
    """Prints text one character at a time with a delay."""
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)


def typing_input(prompt, delay=0.05):
    """Shows prompt with typing effect, then waits for user input."""
    for character in prompt:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    return input()


def clear_screen():
    """Clears the terminal screen."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    clear_screen()
    typing_print("Hello there! This is the typing‑effect in action.\n")
    name = typing_input("What's your name? ")
    typing_print(f"\nNice to meet you, {name}!\n")

# Jack and the Beanstalk


def beanstalk_height(hours):
    height = 100
    for hour in range(2, hours + 1):
        height = height * 1.5 + 30
    return height


for h in [7, 12, 24]:
    print(f"Hour {h}: {beanstalk_height(h):.2f} cm")

# String Slicing

# Defining the alphabet string
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Using indexing to get the first and last characters
firstCharacter = alphabet[0]        # First character (A)
lastCharacter = alphabet[25]        # Last character (Z)

# Returning the full alphabet and the first/last characters
print(alphabet)
print("First character: " + firstCharacter)
print("Last character: " + lastCharacter)

# Using the find() method to find the position of certain letters
posA = alphabet.find("A")
posC = alphabet.find("C")
print("Letter A is at position: " + str(posA))
print("Letter C is at position: " + str(posC))

# Checking if '@' is in the alphabet
if "@" in alphabet:
    print("Letter @ is in the alphabet!!!")
else:
    print("Letter @ is not in the alphabet!!!")

# Trying to find the position of '@' (will return -1 if not found)
posAt = alphabet.find("@")
print("The position of @ in the alphabet is: " + str(posAt))

# Higher or Lower Number Game


def higher_or_lower_number_game():
    """Play one round of Higher or Lower (number between 1 and 100)."""
    secret = random.randint(1, 100)
    attempts = 0

    print("\nI've picked a number between 1 and 100. Try to guess it!")
    while True:
        guess_str = input("Your guess: ").strip()
        # validate input
        try:
            guess = int(guess_str)
        except ValueError:
            print("Please enter a whole number (1-100).")
            continue

        if not 1 <= guess <= 100:
            print("Number must be between 1 and 100.")
            continue

        attempts += 1

        if guess < secret:
            print("Higher 🔼")
        elif guess > secret:
            print("Lower 🔽")
        else:
            print(
                f"Correct! 🎉 You guessed the number in {attempts} attempt{'s' if attempts != 1 else ''}.")
            break

        higher_or_lower_number_game()


# The Missing Key
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
while i < b:
    final_value = a + a
print(
    f"The first number ({a}) multiplied by the second number({b} is equal to {final_value})")

# Class Register


def take_register(pupils):
    total = len(pupils)
    present_count = 0

    for pupil in pupils:
        while True:
            status = input(f"Is {pupil} present? (y/n): ").strip().lower()
            if status in ('y', 'n'):
                break
            print("Invalid input. Please enter 'y' for present or 'n' for absent.")

        if status == 'y':
            present_count += 1

    absent_count = total - present_count

    print("\n--- Register Summary ---")
    print(f"Total pupils:   {total}")
    print(f"Present:        {present_count}")
    print(f"Absent:         {absent_count}")


if __name__ == "__main__":
    pupils = ["Joe", "Sonny", "Yassine", "Emma", "Ines",
              "Satveer", "Lily", "Reuben", "Lucy", "Tom", "Shmuunu"]
    take_register(pupils)

# Password generator


def shuffle(s: str) -> str:
    temp = list(s)
    random.shuffle(temp)
    return ''.join(temp)


def generate_password() -> str:
    upper = random.sample(string.ascii_uppercase, 2)
    lower = random.sample(string.ascii_lowercase, 2)
    digits = random.sample(string.digits, 2)
    punctuation = random.sample(string.punctuation, 2)

    all_chars = upper + lower + digits + punctuation
    random.shuffle(all_chars)
    return ''.join(all_chars)


if __name__ == "__main__":
    print(generate_password())


# How old will you be in...
def age_calc():
    year = 2017
    age = int(input("How old are you? "))

    for i in range(1, 51):
        year += 1
        age += 1
        print(f"In {year}, you will be {age} years old.")


age_calc()

# Cake sale

# Prices in GBP
cupcakePrice = 0.40
macaronPrice = 0.50
cheesecakePrice = 0.70

# Step 1: Input quantities from the user
cupcakes = int(input("How many cupcakes do you plan to sell? "))
macarons = int(input("How many macarons do you plan to sell? "))
cheesecake = int(input("How many cheesecake slices do you plan to sell? "))

# Step 2: Calculate total revenue
total = (cupcakes * cupcakePrice +
         macarons * macaronPrice +
         cheesecake * cheesecakePrice)

# Step 3: Display total money raised
print(f"Total money raised = £{total:.2f}")

# --- Extension Task: Profit Calculation ---

expenses = 12.00  # cost of ingredients
profit = total - expenses

# Step 4: Display profit or loss
print(f"Profit = £{profit:.2f}")

# Step 5: Evaluate profit/loss/break even
if profit > 0:
    print("You made a profit!")
elif profit < 0:
    print("You made a loss!")
else:
    print("You broke even!")
