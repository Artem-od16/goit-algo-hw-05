from functools import wraps


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command."

    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    if name.isalpha() and phone.isdigit():
        contacts[name] = phone
        return "Contact added."
    else:
        return "Contact cannot be added. Name  must consist of letters and phone must consist of numbers."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        if phone.isdigit():
            contacts[name] = phone
            return "Contact updated."
        else:
            return "Contact cannot be updated. Phone must consist of numbers."
    else:
        return "Contact not found."


@input_error
def show_contact(args, contacts):
    name = args[0]
    return contacts[name]


@input_error
def show_all(contacts):
    if len(contacts) != 0:
        for name, phone in contacts.items():
            if name != "" and phone != "":
                print(f"Name - {name}, phone - {phone}")
            else:
                continue
    else:
        return "No contacts."
