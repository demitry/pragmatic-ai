"""Простой модуль"""

import pandas as pd


def list_of_belts_in_bjj():
    """Возвращает список поясов бразильского джиу-джитсу"""
    belts = ["white", "blue", "purple", "brown", "black"]
    return belts


def count_belts():
    """Использует библиотеку Pandas для подсчета числа поясов"""
    belts = list_of_belts_in_bjj()
    df = pd.DataFrame(belts)
    res = df.couпt()
    count = res.values.tolist()[0]
    return count

# from fuпclib.fuпcmod import couпt_belts
# print(couпt_belts())
