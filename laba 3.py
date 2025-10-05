
print("Список квадратов чисел от 1 до 10:")
sq = [x ** 2 for x in range(1, 11)]
print(sq)


print("\n2. Чётные числа от 1 до 20:")
chetka = [x for x in range(1, 20) if x % 2 == 0]
print(chetka)

print("\n3. Слова в верхнем регистре длиннее 3 символов:")
words = ["python", "Java", "c++", "Rust", "go"]
tri = [word.upper() for word in words if len(word) > 3]
print(tri)

print("\n4. Собственный итератор Countdown:")


class Countdown:
    def __init__(self, n):
        self.n = n
        self.current = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 1:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


print("Countdown от 5:")
for x in Countdown(5):
    print(x, end=' ')
print()

print("\n5. Генератор чисел Фибоначчи:")


def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


print("Первые 5 чисел Фибоначчи:")
for num in fibonacci(5):
    print(num, end=' ')
print()

print("\n6. Финансовый калькулятор вкладов:")
from decimal import Decimal, getcontext


def calculate_deposit(initial_amount, interest_rate, years):
    # достаточную точность
    getcontext().prec = 10

    P = Decimal(str(initial_amount))
    r = Decimal(str(interest_rate))
    t = Decimal(str(years))

    #ежемес капитализацией
    S = P * (1 + r / (12 * 100)) ** (12 * t)

    final_amount = S.quantize(Decimal("0.01"))
    profit = (final_amount - P).quantize(Decimal("0.01"))

    return final_amount, profit



initial = 100000.50  # 00000 рублей 50 копеек
rate = 7.5  # .5% годовых
term = 3 # 3 года

final, profit = calculate_deposit(initial, rate, term)
print(f"Начальная сумма: {initial} руб.")
print(f"Ставка: {rate}%")
print(f"Срок: {term} лет")
print(f"Итоговая сумма: {final} руб.")
print(f"Общая прибыль: {profit} руб.")


print("\n7. Работа с дробями:")
from fractions import Fraction

frac1 = Fraction(3, 4)
frac2 = Fraction(5, 6)

print(f"Дробь 1: {frac1}")
print(f"Дробь 2: {frac2}")

addition = frac1 + frac2
subtraction = frac1 - frac2
multiplication = frac1 * frac2
division = frac1 / frac2

print(f"Сложение: {frac1} + {frac2} = {addition}")
print(f"Вычитание: {frac1} - {frac2} = {subtraction}")
print(f"Умножение: {frac1} × {frac2} = {multiplication}")
print(f"Деление: {frac1} ÷ {frac2} = {division}")

print("\n8. Текущая дата и время:")
from datetime import datetime

now = datetime.now()
print(f"Текущая дата и время: {now}")
print(f"Только текущая дата: {now.date()}")
print(f"Только текущее время: {now.time()}")

print("\n9. Разница дат:")
from datetime import date, timedelta

birthday = date(2005, 10, 24)
today = date.today()


days_passed = (today - birthday).days


next_birthday = date(today.year, birthday.month, birthday.day)
if next_birthday < today:
    next_birthday = date(today.year + 1, birthday.month, birthday.day)

days_to_next_birthday = (next_birthday - today).days

print(f"День рождения: {birthday}")
print(f"Сегодня: {today}")
print(f"Дней прошло с момента рождения: {days_passed}")
print(f"Дней до следующего дня рождения: {days_to_next_birthday}")

# ===== 10. DateTime (форматирование строк) =====
print("\n10. Форматирование даты и времени:")


def format_datetime(dt):

    months_ru = {
        1: "января", 2: "февраля", 3: "марта", 4: "апреля",
        5: "мая", 6: "июня", 7: "июля", 8: "августа",
        9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
    }

    day = dt.day
    month = months_ru[dt.month]
    year = dt.year
    time_str = dt.strftime("%H:%M")

    return f"Сегодня {day} {month} {year} года, время: {time_str}"


# Пример использования
current_dt = datetime.now()
formatted = format_datetime(current_dt)
print(formatted)