import time
list_of_reg_num = ['Владимир Петрович', 'Мария Иванова', 'Андрей Осипенко']
sel_num = input("Выберите водителя из списка: " + str(list_of_reg_num) + " ")
if sel_num in list_of_reg_num:
    print("Сейчас вы смотрите информацию по водителю: " + sel_num)
    time.sleep(0.5)
else:
    print("Такого водителя не существует, попробуйте заново")
    exit()
dohod = int(input("Чистый доход водителя в кроннах: "))
bonus = int(input("Введите колиство бонусов(будут поделены на 50%): "))
orenda = int(input("Введите затраты на аренду: "))
time.sleep(0.5)
print("Также будут вычтены 700 кронн за гараж")
time.sleep(1)
def present():
    result = dohod - (bonus * 0.5)
    amount = result - (orenda - 700)
    print("Чистый доход работника составляет " + str(amount))
    return result, amount
present()