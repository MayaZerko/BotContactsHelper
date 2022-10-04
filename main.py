

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

