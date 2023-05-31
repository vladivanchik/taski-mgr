import time
reg_num = input("Введите регистрационный номер: ")
dohod = int(input("Чистый доход водителя в кроннах: "))
bonus = int(input("Введите колиство бонусов(будут поделены на 50%): "))
orenda = int(input("Введите затраты на аренду: "))
time.sleep(0.5)
print("Также будут вычтены 700 кронн за гараж")
time.sleep(1)
print("Регистрационный номер по которму вы смотрите информацию: " + reg_num)
def present():
    result = dohod - (bonus * 0.5)
    amount = result - (orenda - 700)
    print("Чистый доход работника составляет " + str(amount))
    return result, amount
present()