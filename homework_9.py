CONTACT_LIST = {}

"""
Декоратор винятків.
"""
def input_error(func):
    def miss_name(command):
        try:
            res = func(command)
            if res == None:
                print('Enter user name')
        except (KeyError, IndexError):
            print("Give me name and phone please!")     
    return miss_name
    
""" 
Функції обробники команд — handler, що відповідають
за безпосереднє виконання команд. 
"""
def greeting(word):
    print('How can I help you?')   


@input_error
def add_contacts(contact):
    add_contact = contact.split(' ') 
    CONTACT_LIST.update({add_contact[1]: add_contact[2]})
    return CONTACT_LIST

@input_error
def change_contact(number):
    new_number = number.split(' ')
    CONTACT_LIST[new_number[1]] = new_number[2]
    return CONTACT_LIST

@input_error
def show_phone(name):
    new_name = name.split(' ')
    number = CONTACT_LIST.get(new_name[1])
    print(number)


def show_all(list_new):
    print(CONTACT_LIST)


def finish(end):
    print('Good bye!')
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
        if command.find(key) >= 0:
            return action(command)
    print("You input wrong command! Try again")


"""
Цикл запит-відповідь. Ця частина програми відповідає за отримання від користувача даних та 
повернення користувачеві відповіді від функції-handlerа.
"""
def main():
    while True:
        action = input("Please, input your command...") 
        new_action = action.casefold()
        parser_command(new_action)


if __name__ == '__main__':
    main()