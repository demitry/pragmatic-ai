# Классы
# Различия классов и функций
# Ключевые различия классов и функций:
# * функции гораздо легче обсуждать;
# * состояние функций (обычно) существует лишь внутри функции,
#   а состояние класса может сохраняться и за ее пределами;
# * классы предлагают более высокий уровень абстракции за счет повышения сложности.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
