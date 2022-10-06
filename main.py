contacts_dict = {}


def input_error(function):
    """
    Створюємо декоратор для обробки помилок, котрі можуть виникнути через
    ввід користувача.
    :param function: Функція вводу від користувача.
    :return: Або роботу функції або текст з помилкою, для повторного вводу.
    """
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except KeyError:
            return 'Wrong name'
        except ValueError:
            return ValueError.args[0]
        except IndexError:
            return 'Pls print: name and number'
        except TypeError:
            return 'Wrong command.'

    return wrapper


@input_error
def hello_func():
    """
    При отриманні команди привіт- маємо зреагувати правильно.
    :return:
    """
    return 'How can I help you?'


@input_error
def exit_func():
    """
    При отриманні слів про вихід з боту- маємо його закрити.
    :return:
    """
    quit()


@input_error
def add_func(name, phone):
    """
    Додавання нового контакту.
    :param name: Ім'я контакту.
    :param phone: Телефон контакту.
    :return: Відповідь, що контакт створено.
    """
    contacts_dict[name] = phone


@input_error
def change_func(name, phone):
    """
    Зміна вже існуючого контактного номера.
    :param name: Контакт в котрому потрібно провести зміни.
    :param phone: Новий номер для контакту.
    :return: Відповідь про зміни.
    """
    contacts_dict[name] = phone


@input_error
def search_func(name):
    """
    Коли користувач шукає конкретний контакт за ім'ям.
    :param name: Контакт котрий шукаємо.
    :return: Номер контакту.
    """
    contacts_dict.get(name)


@input_error
def show_func():
    """
    Показуємо всю книгу контактів створену раніше.
    :return:
    """
    print(contacts_dict)


COMMANDS_DICT = {
    'hello': hello_func,
    'exit': exit_func,
    'close': exit_func,
    'good bye': exit_func,
    'add': add_func,
    'change': change_func,
    'show all': show_func
}


def change_input(user_input):
    new_input = user_input
    data = ''
    for key in COMMANDS_DICT:
        if user_input.strip().lower().startswith(key):
            new_input = key
            data = user_input[len(new_input):]
            break
    if data:
        return reaction_func(new_input)(data)
    else:
        return reaction_func(new_input)()


def reaction_func(reaction):
    return COMMANDS_DICT.get(reaction, break_func)


def break_func():
    """
    Якщо користувач ввів якусь тарабарщину- повертаємо відповідну відповідь
    :return: Неправильна команда
    """
    print('Wrong enter.')


def main():
    """
    Основна логика усього застосунку. Отримуємо ввід від користувача
    і відправляємо його в середину застосунку на обробку.
    :return:
    """
    while True:
        """
        Просимо користувача ввести команду для нашого бота
        Також тут же вимикаємо бота якщо було введено відповідну команду
        """

        user_input = input('Enter command for bot: ')
        result = change_input(user_input)
        print(result)
        if result == 'good bye':
            break


if __name__ == '__main__':
    main()
