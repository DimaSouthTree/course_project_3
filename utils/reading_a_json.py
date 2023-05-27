import json
import datetime



def load_operations():
    """
    читает файл operations.json и записывает в переменную data_operations
    :return: переменную data_operations (список ловарей)
    """
    with open("../operations.json", "r", encoding="utf-8") as element:
        data_operations = json.load(element)
        return data_operations


print(load_operations())

all_data_operations = load_operations()


def receiving_executed_operation():
    executed_list = []

    for item in all_data_operations:
        if item.get('state') == "EXECUTED":
            executed_list.append(item)
    return executed_list



all_data_executed_operation = receiving_executed_operation()
print(all_data_executed_operation)

def receiving_date_operation():
    date_list = []

    for item in all_data_executed_operation:
        date_list.append(item["date"])
    return date_list


print(receiving_date_operation())
