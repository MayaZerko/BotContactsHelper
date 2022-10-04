CONTACTS = {}


def hello_func():
    print('How can I help you?')


def exit_func():
    quit()


def add_func(name, phone):
    CONTACTS[name] = phone


def change_func(name, phone):
    CONTACTS[name] = phone

def search_func(name):
    CONTACTS.get(name)

def show_func():
    print(CONTACTS)

COMMANDS_DICT = {
    'hello': hello_func,
    'exit': exit_func,
    'close': exit_func,
    'good bye': exit_func,
    'add': add_func,
    'change': change_func,
    'show all': show_func
}


def main():
    while True:
        """
        Просимо користувача ввести команду для нашого бота
        Також тут же вимикаємо бота якщо було введено відповідну команду
        """

        user_input = input('Enter command for bot: ')
        if user_input == 'Good bye':
            break


if __name__ == '__main__':
    main()
