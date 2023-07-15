amount = 0
tickets = int(input("Сколько билетов вы хотите купить?\n"))
for age in range(tickets):
    age = int(input("Введите возраст посетителя\n"))
    if age <18:
        amount +=0
    elif age >=18 and age <= 25:
        amount += 990
    else: amount += 1390
if amount == 0:
    print ("Проходите, детки, на конференцию")
else: print ("Кол-во билетов:", tickets, "шт")
if tickets > 3:
    discount = amount * 0.1
    print ("Скидка составляет:" "%.2f" % discount, "руб")
    print("К оплате с учетом скидки:", "%.2f" % (amount-discount), "руб")
if tickets <4:
    nodiscount = amount
    print ("К оплате:", "%.2f" % nodiscount, "руб.")
