phone_book = {}


def add_contact(name):
    if name in phone_book:
        pass
    else:
        phone_book[name] = {} 


def add_number(name, number):
    add_contact(name)
    if 'numbers' in phone_book[name]:
        if number in phone_book[name]['numbers']:
            pass
        else:
            phone_book[name]['numbers'].append(number)
    else:
        phone_book[name]['numbers'] = [number]
    print('number added')


def add_email(name, email):
    add_contact(name)
    if 'emails' in phone_book[name]:
        if email in phone_book[name]['emails']:
            pass
        else:
            phone_book[name].append(email)
    else:
        phone_book[name]['emails'] = [email]
    print("email added")
  

def del_name(name):
    if name in phone_book:
        del(phone_book[name])
        print('number deleted')
    else:
        print("number didn't exist")


def search_name(name):
    if name in phone_book:
        print(phone_book[name])
    else:
        print("name didn't exist")


def del_number(number):
    for name in phone_book:
        if number in phone_book[name]['numbers']:
            i = phone_book[name]['numbers'].index(number)
            del(phone_book[name]['numbers'][i])
            print('number deleted')
            if phone_book[name]['numbers'] == []:
               del(phone_book[name]['numbers'])
            return
    print("number didn't exist")


def print_phone_book():
    for name in phone_book:
        print(name, ':', phone_book[name])


def search_number(number):
    for name in phone_book:
        if 'numbers' in phone_book[name]:
            if number in phone_book[name]['numbers']:
                print(name)
                return
    print('number did not exist')


def change_number(name, old_number, new_number):
    for name in phone_book:
        if 'numbers' in phone_book[name]:
            if old_number in phone_book[name]['numbers']:
                del_number(old_number)
                add_number(name, new_number)
        else:
            print("number did not exitst")


def change_name(old_name, new_name):
    if old_name in phone_book:
        phone_book[new_name] = phone_book[old_name]
        del(phone_book[old_name])
    else:
        print("name didn't exist")
        

add_number("abbas", "02345972212")
add_number("mohammd", "01239407121")
