from utils.reading_a_json import receiving_executed_operation, sort_operations_by_date, format_date, account_mask

a = [{'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05T12:04:13.781725',
      'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}},
      'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'}, {
         "id": 27192367, "state": "CANCELED", "date": "2018-12-24T20:16:18.819037",
         "operationAmount": {"amount": "991.49", "currency": {"name": "руб.", "code": "RUB"}},
         "description": "Перевод со счета на счет", "from": "Счет 71687416928274675290",
         "to": "Счет 87448526688763159781"}]
d = [{'id': 801684332, 'state': 'CANCELED', 'date': '2019-11-05T12:04:13.781725',
      'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}},
      'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'}, {
         "id": 27192367, "state": "CANCELED", "date": "2018-12-24T20:16:18.819037",
         "operationAmount": {"amount": "991.49", "currency": {"name": "руб.", "code": "RUB"}},
         "description": "Перевод со счета на счет", "from": "Счет 71687416928274675290",
         "to": "Счет 87448526688763159781"}]

b = [{'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05T12:04:13.781725',
      'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}},
      'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'}]

c = [{'id': 596171168, 'state': 'EXECUTED', 'date': '2018-07-11T02:26:18.671407',
      'operationAmount': {'amount': '79931.03', 'currency': {'name': 'руб.', 'code': 'RUB'}},
      'description': 'Открытие вклада', 'to': 'Счет 72082042523231456215'},
     {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916',
      'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}},
      'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658',
      'to': 'Visa Platinum 8990922113665229'}]
e = [{'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916',
      'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}},
      'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658',
      'to': 'Visa Platinum 8990922113665229'},
     {'id': 596171168, 'state': 'EXECUTED', 'date': '2018-07-11T02:26:18.671407',
      'operationAmount': {'amount': '79931.03', 'currency': {'name': 'руб.', 'code': 'RUB'}},
      'description': 'Открытие вклада', 'to': 'Счет 72082042523231456215'}]


def test_receiving_executed_operation():
    assert receiving_executed_operation(a) == b
    assert receiving_executed_operation(d) == []
    assert receiving_executed_operation(d) != b


def test_sort_operations_by_date():
    assert sort_operations_by_date(a, 2) != a
    assert sort_operations_by_date(e, 2) == c


def test_format_date():
    assert format_date("2019-08-19T16:30:41.967497") == "19.08.2019"
    assert format_date("2019-08-19T16:30:41.967497") != "19-08-2019"


def test_account_mask():
    assert account_mask('Maestro 1596837868705199') == "Maestro 1596 ** **** 5199"
    assert account_mask('Visa Classic 2842837868709012') == "Visa Classic 2842 ** **** 9012"
    assert account_mask('Счет 75106830613657916952') == 'Счет **6952'
    assert account_mask('Maestro 1596837868705199') != " "
