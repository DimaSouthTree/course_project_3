import json
from datetime import datetime
from operator import itemgetter


def load_operations():
    """
    читает файл operations.json и записывает в переменную data_operations
    :return: переменную data_operations (список ловарей)
    """
    with open("../operations.json", "r", encoding="utf-8") as element:
        data_operations = json.load(element)
        return data_operations


def receiving_executed_operation(data):
    """
    принимает масиив операций и сортирует с добавлением в список выполненные операции
    :return: список массива выполненых операций
    """
    executed_list = []

    for item in data:
        if item.get('state') == "EXECUTED":
            executed_list.append(item)
    return executed_list


def sort_operations_by_date(data, last_count):
    """
    принимает масиивы выполненных операций и сортирует их по дате в порядке возрастания
    :return: массив последних пять выполненных операций
    """
    data = sorted(data, key=itemgetter("date"))
    return data[-last_count:]


def format_date(date):
    """
    :param date: принимает значение ключа 'date' и форматирует дату в нужный формат для вывода
    :return: дату в виде строки в нужном формате
    """
    dt = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return dt.strftime('%d.%m.%Y')


def account_mask(account):
    """
    :param account:значение ключа 'from' в виде строки, если в строке есть слово Счет то делает модификатор строки счета
    иначе делает модификатор строки под карты
    :return: модификатор строки
    """
    if len(account) == 0:
        return account
    if 'Счет' in account:
        check = "".join([account[:-20], '**', account[-4:]])
        return check
    else:
        check_card = " ".join([account[:-12], '**', '****', account[-4:]])
        return check_card


# Вызываем функции и записываем результаты в переменные
all_data_operations = load_operations()
all_data_executed_operation = receiving_executed_operation(all_data_operations)
five_executed_operation = sort_operations_by_date(all_data_executed_operation, 5)

# проходимся по массиву последних пяти выполненных операций и выводим данные об операциях
for item in five_executed_operation:
    data_operationAmount = item['operationAmount']
    data_operationAmount_currency = data_operationAmount['currency']
    key_value_from = item.get('from', "")
    key_value_to = item.get('to', "")

    date = format_date(item['date'])
    mask_from = account_mask(key_value_from)
    mask_to = account_mask(key_value_to)
    if len(mask_from) != 0:
        mask_from += " -> "

    print(date, item['description'])
    print(mask_from, mask_to, sep="")
    print(data_operationAmount['amount'], data_operationAmount_currency['name'])
    print("")
