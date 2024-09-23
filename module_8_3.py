class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    '''
    Класс Car должен обладать следующими свойствами:
    Атрибут объекта model - название автомобиля (строка).
    Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
    Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность.
    Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
    Атрибут __numbers - номера автомобиля (строка).
    Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность.
    Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
    Классы исключений IncorrectVinNumber и IncorrectCarNumbers,
    объекты которых обладают атрибутом message - сообщение, которое будет выводиться при
    выбрасывании исключения.
    '''
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers
    def __is_valid_vin(self, vin):
        '''
        Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер',
        если передано не целое число. (тип данных можно проверить функцией isinstance).
        Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера',
        если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
        Возвращает True, если исключения не были выброшены.
        '''
        if isinstance(vin, int):
            if vin > 1000000 and vin < 9999999:
                return True
            else:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            raise IncorrectVinNumber('Некорректный тип vin номер')
    def __is_valid_numbers(self, numbers):
        '''
        Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров',
        если передана не строка. (тип данных можно проверить функцией isinstance).
        Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера',
        переданная строка должна состоять ровно из 6 символов.
        Выбрасывает исключение IncorrectCarNumbers  с сообщением 'Некорректный номер',
        если в переаной строке нет хотя бы одной цифры или хотя бы одной буквы.
        Возвращает True, если исключения не были выброшены.
        '''
        PUNKT = str('.,/!@#$%^&*()_+=}{][| ')
        if isinstance(numbers, str):
            if len(numbers) == 6:
                numb = 0
                for i in range(0, 9):
                    if numbers.count(str(i)):
                        numb += 1
                punkt = 0
                for i in PUNKT:
                    if numbers.count(i):
                        punkt += 1
                if numb > 0 and numb < 5 and punkt == 0:
                    return True
                else:
                    raise IncorrectCarNumbers('Некорректный номер')
            else:
                raise IncorrectCarNumbers('Неверная длина номера')
        else:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'hub123')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')