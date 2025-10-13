#1
# change_cash = float(input('Введите сумму для обмена: '))
# currency = {'USD': 'USD', 'EUR': 'EUR'}
# choose_currency = input('Выбери валюту (USD, EUR): ').upper()
#
# if choose_currency == 'USD':
#     cash = change_cash * 0.86
# else:
#     cash = change_cash * 1.17
#
# print(cash)

#2
# temperature = float(input('Введите температуру: '))
#
# if temperature >= 100:
#     print("Состояние воды: Газообразное.")
# if 0 < temperature < 100:
#     print("Состояние воды: Жидкость.")
# elif temperature <= 0:
#     print("Состояние воды: Лёд.")

#3
weight = float(input('Введите массу: m = '))
speed = float(input('Введите скорость: v = '))
kinetic_energy = 0,5 * weight * (speed ** 2)

if speed == 0:
    print('Состояние - покоя.')
if speed < 10:
    print('Состояние - медлетнное движение.')
else:
    print('Состояние - быстрое движение.')
print(f"\nКинетическая энергия: {kinetic_energy:} ДЖ")





