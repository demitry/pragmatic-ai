# Использование метода apply в библиотеке Pandas. Последний мой урок
# на тему функций - использование их для обработки объектов DataFrame
# библиотеки Pandas. Один из базовых принципов Pandas - применение
# операции apply к столбцу вместо организации итераций по всем значениям.
# Этот пример демонстрирует округление всех чисел до целых:

import pandas as pd

iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
print(iris.head())

iris['rounded_sepal_length'] = iris[['sepal_length']].apply(pd.Series.round)
print(iris.head())


def multiply_by_100(x):
    """Умножает на 100"""
    return x * 100


iris['100x_sepal_length'] = iris[['sepal_length']].apply(multiply_by_100)
print(iris.head())
