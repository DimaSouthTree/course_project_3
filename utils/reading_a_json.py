import json
from datetime import datetime
import datetime as DT
from operator import itemgetter


def load_operations():
    """
    читает файл operations.json и записывает в переменную data_operations
    :return: переменную data_operations (список ловарей)
    """
    with open("../operations.json", "r", encoding="utf-8") as element:
        data_operations = json.load(element)
        return data_operations


all_data_operations = load_operations()


def receiving_executed_operation():
    executed_list = []

    for item in all_data_operations:
        if item.get('state') == "EXECUTED":
            executed_list.append(item)
    return executed_list


all_data_executed_operation = receiving_executed_operation()


def sort_operations_by_date():
    all_data_executed_operation_sort = sorted(all_data_executed_operation, key=itemgetter("date"))
    return all_data_executed_operation_sort[-5:]


print(sort_operations_by_date())
five_executed_operation = sort_operations_by_date()

# Пример вывода для одной операции:
# 14.10.2018 Перевод организации
# Visa Platinum 7000 79** **** 6361 -> Счет **9638
# 82771.72 руб.

# def output_of_the_last_five():
for item in five_executed_operation:
    date = item['date']
    dt = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    format_date = dt
    format_date_string = format_date.strftime('%m.%d.%Y')

    data_operationAmount = item['operationAmount']
    data_operationAmount_currency = data_operationAmount['currency']

    if item['description'] == 'Открытие вклада':
        print(format_date_string, item['description'])
        print("->", item['to'][0:4], "**" + item['to'][-4:])
        print(data_operationAmount['amount'], data_operationAmount_currency['name'])
        print("")
    if item['description'] == 'Перевод со счета на счет':
        print(format_date_string, item['description'])
        print(item['from'][0:4], "**" + item['from'][-4:], "->", item['to'][0:4], "**" + item['to'][-4:])
        print(data_operationAmount['amount'], data_operationAmount_currency['name'])
        print("")
    if item['description'] == 'Перевод организации':
        print(format_date_string, item['description'])
        print(item['from'][0:11] + item['from'][12:16] + item['from'][16:18] + "**", "****", item['from'][-4:], "->",
              item['to'][0:4], "**" + item['to'][-4:])
        print(data_operationAmount['amount'], data_operationAmount_currency['name'])
        print("")

d = {'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05T12:04:13.781725',
     'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}},
     'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'}
