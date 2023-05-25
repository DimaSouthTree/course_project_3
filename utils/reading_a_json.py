import json


def load_operations():
    """
    читает файл operations.json и записывает в переменную data_operations
    :return: переменную data_operations (список ловарей)
    """
    with open("../operations.json", "r", encoding="utf-8") as element:
        data_operations = json.load(element)
        return data_operations
