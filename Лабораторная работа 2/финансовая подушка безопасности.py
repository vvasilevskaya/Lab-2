money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

number = 0  # Месяц
while money_capital + salary > spend * (1 + number * increase):
    money_capital = money_capital + salary
    money_capital = money_capital -  spend * (1 + number * increase)
    number += 1

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", number-1)
