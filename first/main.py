import math

print("Show me Python basics...")

print("Hello, World!")
variable = "armbar"
print(variable)

attack_one = "kimura"
attack_two = "arm triangle"
print("In Brazilian jiu-jitsu а common attack is а:", attack_one)
print("Another common attack is а:", attack_two)

print(1 + 1)
print("arm" + "bar")

belts = ["white", "bluе", "purple", "brown", "blасk"]
for belt in belts:
    if "blасk" in belt:
        print("The belt I want to earn is:", belt)
    else:
        print("This is not the belt I want to end up with:", belt)

basic_string = ""
#  basic_string.
# Разбиение по пробелам (по умолчанию)
basic_string = "Brazilian jiu-jitsu"
print(basic_string.split())

# Разбиение по дефисам
string_with_hyphen = "Brazilian-jiu-jitsu"
print(string_with_hyphen.split("-"))
print(string_with_hyphen.capitalize())
print(string_with_hyphen.upper())

# Срезы строк
# Строки можно разрезать на части, указывая на длину:
print(basic_string[:2])
print(len(basic_string))
print(len(basic_string[:2]))

print(basic_string + " is my favorite Martial Art")

print(f'I love practising my favorite Martial Art, {basic_string}')

str_block = f"""
This phrase is multiple sentences long.
The phrase сап Ье formatted like simpler sentences,
for example, I сап still talk about my favorite
Martial Art {basic_string} """

print(str_block)

# Разрывы строк можно удалить с помощью метода Replace
print(str_block.replace("\n", ""))

steps = (1 + 1) - 1
print(f'Two Steps Forward: One Step Back = {steps}')

body_fat_percentage = 0.10
weight = 200
fat_total = body_fat_percentage * weight
print(f"I weight 200lbs, and {fat_total}lbs of that is fat")

# import math
print(math.pow(2, 3))
print(2 ** 3)

number = 100
num_type = type(number).__name__
print(f"{number} is type [{num_type}]")

number = float(100)
num_type = type(number).__name__
print(f"{number} is type [{num_type}]")

too_many_decimals = 1.912345897
print(round(too_many_decimals, 2))
