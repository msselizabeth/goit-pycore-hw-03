"""
Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином і в певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей. Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.
"""

import random


def get_numbers_ticket(min, max, quantity):
    # Validating params
    if (min < 1) or (max > 1000):
        print("Invalid min or max params.")
        return []
    if min > max:
        print("Min cannot be more than Max")
        return []
    if quantity > (max - min):
        print("Quantity cannot be more than list length")
        return []

    #  create a list of nums in min-max range
    nums = list(range(min, max + 1))

    # Random choice of uniqe nums from the list, and sorting
    result = random.sample(nums, k=quantity)
    result.sort()

    return result


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(0, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(10, 4, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(10, 15, 7)
print("Ваші лотерейні числа:", lottery_numbers)
