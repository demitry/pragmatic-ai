import math

print("Show me Python basics...")

print("Hello, World!")
variable = "armbar"
print(variable)

attack_one = "kimura"
attack_two = "arm triangle"
print("In Brazilian jiu-jitsu а common attack is а:", attack_one)
print("Another common attack is а:", attack_two)

belts = ["white", "bluе", "purple", "brown", "blасk"]
for belt in belts:
    if "blасk" in belt:
        print("The belt I want to earn is:", belt)
    else:
        print("This is not the belt I want to end up with:", belt)

print(1 + 1)
print("arm" + "bar")

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

submissions = {"armbar": "upper_body",
               "arm_triangle": "upper_body",
               "heel_hook": "lower_body",
               "knee_bar": "lower_body"}

for submission, body_part in submissions.items():
    print(f'The {submission} is ап attack '
          f'оn the {body_part}')

print(f"These are upper_body submission attacks "
      f"in Brazilian jiu-jitsu:")
for submission, body_part in submissions.items():
    if body_part == "upper_body":
        print(submission)

print(f"There are keys: {submissions.keys()}")
print(f"There are values: {submissions.values()}")

# Списки могут включать в качестве
# элементов словари, точно так же,
# как и словари могут включать списки.

list_of_bjj_positions = \
    ["mount", "full-guard",
     "half-guard", "turtle",
     "side-control", "rear-mount",
     "knee-on-belly", "north-south",
     "open-guard"]

for position in list_of_bjj_positions:
    if "guard" in position:
        print(position)

# Можно выбирать элементы списков посредством срезов:

print(f'First position: {list_of_bjj_positions[:1]}')
print(f'Last position: {list_of_bjj_positions[-1:]}')
print(f'First three positions: {list_of_bjj_positions[0:3]}')


def favorite_martial_art():
    return "bjj"


favorite_martial_art()

print(favorite_martial_art.__doc__)


def practice(times):
    print(f"I like to practice {times} times а day")


practice(2)


# Позиционные # аргументы функций обрабатываются в порядке их описания.
# Поэтому их можно легко создавать и легко же перепутать.

def practice(times, technique, duration):
    print(f"I like to practice {technique},"
          f" {times} times а day, "
          f"for {duration} minutes")


practice(3, "leg locks", 45)


# Именованные аргументы: обрабатываются по ключу или значению,
# могут иметь значения по умолчанию

def practice(times=2, technique="kimura", duration=60):
    print(f"I like to practice {technique}, "
          f"{times} times а day, "
          f"for {duration} minutes")


practice()


# **kwargs и *args. Синтаксисы **kwargs или *args позволяют передавать
# в функции динамические аргументы. Однако применять эти виды синтаксиса
# следует осмотрительно, поскольку они затрудняют понимание
# кода. При использовании там, где это целесообразно, они предоставляют
# широкие возможности.

def attack_techniques(**kwargs):
    for name, attack in kwargs.items():
        print(f"This is an attack I would like to practice: {attack}")


attack_techniques(arm_attack="kimura",
                  leg_attack="straight_ankle_lock",
                  neck_attack="arm_triangle")

# Передача функции словаря именова1П1ых арrумеmов.
# Синтаксис **kwargs можно использовать для передачи всех аргументов сразу:

attacks = {"arm_attack": "kimura",
           "leg_attack": "straight_ankle_lock",
           "neck_attack": "arm_triangle"}

attack_techniques(**attacks)


# Передача фуккций в качестве аргументов.
def attack_location(technique):
    """Возвращает место применения приема"""
    attacks = {"kimura": "arm_attack",
               "straight_ankle_lock": "leg_attack",
               "arm_triangle": "neck_attack"}
    if technique in attacks:
        return attacks[technique]
    return "Unknown"


print(attack_location("kimura"))
print(attack_location("bear hug"))


def multiple_attacks(attack_location_function):
    """Принимает на входе функцию распределения приемов
    по категориям и возвращает место применения приема"""
    new_attacks_list = ["rear_naked_choke", "americana", "kimura"]
    for attack in new_attacks_list:
        attack_location = attack_location_function(attack)
        print(f"The location of attack {attack} is {attack_location}")


print(multiple_attacks(attack_location))

# Замыкания и каррирование функций.
# Замыкания (closures) - функции, содержащие другие функции.
# В языке Python их часто применяют для отслеживания состояния.
# В приведенном ниже примере внешняя функция
# attack_counter отслеживает число атакующих приемов.
# Внутренняя функция attack_filter использует ключевое слово nonlocal языка Python 3 для
# изменения значения переменной во внешней функции.
# Такой подход носит название каррирования функций (functional currying)
# и позволяет создавать на основе общих функций специализированные.
# Как показано ниже, подобные функции могут лечь в основу простой компьютерной игры
# или подсчета статистики поединка в смешанных единоборствах:

print("--- closures and currying ---")


def attack_counter():
    """Подсчитывает количество атак на конкретную половину тела"""
    lower_body_counter = 0
    upper_body_counter = 0

    def attack_filter(attack):
        nonlocal lower_body_counter
        nonlocal upper_body_counter
        attacks = {"kimura": "upper_body",
                   "straight_ankle_lock": "lower_body",
                   "arm_triangle": "upper_body",
                   "keylock": "upper_body",
                   "knee_bar": "lower_body"}
        if attack in attacks:
            if attacks[attack] == "upper_body":
                upper_body_counter += 1
        if attacks[attack] == "lower_body":
            lower_body_counter += 1
        print(f"Upper Body Attacks {upper_body_counter}, "
              f"Lower Body Attacks {lower_body_counter}")

    return attack_filter


fight = attack_counter()

fight("kimura")
fight("knee_bar")
fight("keylock")


# Функции, использующие ключевое слово yield (генераторы).
# Отложенное вычисление
# Генераторы выдают значение в нужный момент времени.
# Нижеприведенный пример возвращает бесконечную случайную последовательность
# атакующих приемов. Отложенность здесь заключается в том,
# что, хотя количество значений бесконечно,
# возвращаются они только при вызове функции.

def lazy_return_random_attacks():
    """Каждый раз возвращает атакующие приемы"""
    import random
    attacks = {"straight_ankle_lock": "lower_body",
               "kimura": "upper_body",
               "arm_triangle": "upper_body",
               "keylock": "upper_body",
               "knee_bar": "lower_body"}
    while True:
        random_attack = random.choices(list(attacks.keys()))
        yield random_attack


attack = lazy_return_random_attacks()
print(next(attack))

print("---")
attacks = {"kimura": "upper_body",
           "straight_ankle_lock": "lower_body",
           "arm_triangle": "upper_body",
           "keylock": "upper_body",
           "knee_bar": "lower_body"}

for _ in range(10):
    print(next(attack))


# Декораторы: функции, служащие адаптерами для других функций.
def randomized_speed_attack_decorator(function):
    """Вносит элемент случайности в скорость атак"""
    import time
    import random

    def wrapper_func(*args, **kwargs):
        sleep_time = random.randint(0, 3)
        print(f"Attacking after {sleep_time} seconds")
        time.sleep(sleep_time)
        return function(*args, **kwargs)

    return wrapper_func


@randomized_speed_attack_decorator
def lazy_return_random_attacks():
    """Каждый раз возвращает атакующие приемы"""
    import random
    attacks = {"kimura": "upper_body",
               "straight_ankle_lock": "lower_body",
               "arm_triangle": "upper_body",
               "keylock": "upper_body",
               "knee_bar": "lower_body"}

    while True:
        random_attack = random.choices(list(attacks.keys()))
        yield random_attack


for _ in range(10):
    print(next(lazy_return_random_attacks()))

# test-pandas, see test-pandas.py

# TODO: import from my module
# import sys; sys.path.appeпd(" .. ")
# from fuпclib import fuпcmod
# fuпcmod.list_of_belts_iп_bjj()
