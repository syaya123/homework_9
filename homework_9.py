CONTACT_LIST = {}

"""
Декоратор винятків.
"""
def input_error(func):
    def miss_name(command):
        try:
            res = func(command)
            if res == None:
                return 'Enter user name. The first letter is capital, and the rest are small.'
            return res
        except (KeyError, IndexError):
            return 'Give your name and phone number, please!'   
    return miss_name
    
""" 
Функції обробники команд — handler, що відповідають
за безпосереднє виконання команд. 
"""
def greeting(word):
    return 'How can I help you?'


@input_error
def add_contacts(contact):
    add_contact = contact.split(' ') 
    CONTACT_LIST.update({add_contact[1]: add_contact[2]})
    return f'You add name {add_contact[1]} and telephone number {add_contact[2]}'

@input_error
def change_contact(number):
    new_number = number.split(' ')
    CONTACT_LIST[new_number[1]] = new_number[2]
    return f'You change contact of {new_number[1]}'

@input_error
def show_phone(name):
    new_name = name.split(' ')
    number = CONTACT_LIST.get(new_name[1])
    return number


def show_all(list_new):
    return CONTACT_LIST


def finish(end):
    exit()  

dict_command = {'hello': greeting,
    'add': add_contacts,
    'change': change_contact,
    'phone': show_phone,
    'show all': show_all,
    'good bye': finish,
    'close': finish,
    'exit': finish
}

"""
Парсер команд.
Частина, яка відповідає за розбір введених користувачем рядків, 
виділення з рядка ключових слів та модифікаторів команд.
"""
def parser_command(command: str)->str:

    for key, action in dict_command.items():
        new_command = command.casefold()
        if new_command.find(key) >= 0:
            return action(command)
    return 'You input wrong command! Please, try again'


"""
Цикл запит-відповідь. Ця частина програми відповідає за отримання від користувача даних та 
повернення користувачеві відповіді від функції-handlerа.
"""
def main():
    while True:
        action = input("Please, input your command...") 
        if 'exit' or 'good bye' or 'close':
            print ('Good bye!')
        result = parser_command(action)
        print(result)


if __name__ == '__main__':
    main()