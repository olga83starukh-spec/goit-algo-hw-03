# Перше завдання: Написати функцію, яка приймає дату у форматі "РРРР-ММ-ДД" і
# повертає кількість днів від цієї дати до сьогоднішнього дня. Якщо дата введена неправильно,
# функція повинна повернути повідомлення про помилку.
from datetime import datetime
def get_days_from_today(date_str):
    try:
        requested_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        current_date = datetime.today().date()
        difference = current_date - requested_date
        return difference.days
    except ValueError:
        return "Помилка: Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'."

print(get_days_from_today('2021-10-09'))
        
# Друге завдання:Щоб виграти головний приз лотереї, необхідний збіг кількох номерів 
# на лотерейному квитку з числами, що випали випадковим чином і в певному діапазоні
# під час чергового тиражу. Наприклад, необхідно вгадати шість чисел від 1 до 49 чи 
# п'ять чисел від 1 до 36 тощо.
# Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе 
# генерувати набір унікальних випадкових чисел для таких лотерей.
# Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі
#  випадкові числа в наборі повинні бути унікальні.

from random import randint
def get_numbers_ticket(min, max, quantity):
    if (
        min < 1 or
        max > 1000 or
        quantity <1 or
        quantity > (max - min + 1)
    ):
        return []
    
    result_set = set()
    while len(result_set) < quantity:
        result_set.add(randint(min, max))
    return sorted(result_set)
print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, 36, 5))


# Третє завдання (не обов'язкове)



# У вашій компанії ведеться активна маркетингова кампанія за допомогою SMS-розсилок.
#  Для цього ви збираєте телефонні номери клієнтів із бази даних, але часто стикаєтеся з тим,
#  що номери записані у різних форматах. Наприклад:

# "    +38(050)123-32-34"
# "     0503451234"
# "(050)8889900"
# "38050-111-22-22"
# "38050 111 22 11   "

# Ваш сервіс розсилок може ефективно відправляти повідомлення лише тоді, коли номери 
# телефонів представлені у коректному форматі. Тому вам необхідна функція, яка автоматично 
# нормалізує номери телефонів до потрібного формату, видаляючи всі зайві символи та додаючи 
# міжнародний код країни, якщо потрібно.

import re
def normalize_phone_number(phone_number):
    cleaned_number = re.sub(r'\D', '', phone_number)
    if not cleaned_number.startswith('+'):
        if cleaned_number.startswith('38'):
            cleaned_number = '+' + cleaned_number
        else:
            cleaned_number = '+38' + cleaned_number
        return cleaned_number
phone_number = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]
for phone in phone_number:
    result = normalize_phone_number(phone)
    print(result)



    
