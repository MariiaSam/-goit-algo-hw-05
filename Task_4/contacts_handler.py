def add_contact(args, contacts):
    if len(args) != 2:
        return 'Invalid arguments. Usage: add name and phone'
    name, phone = args
    contacts[name] = phone
    return 'Contact added.'


def change_contact(contacts, name, phone):
    if name not in contacts:
        return f'Contact with this name {name} was not found.'
    contacts[name] = phone
    return 'Contact updated.'


def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        return f'Contact with this name {name} was not found.'


def show_all(contacts):
    if contacts:
        return '\n'.join(f'{name}: {phone}' for name, phone in contacts.items())
    else:
        return 'Contact was not found.'