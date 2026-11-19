def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            return str(error)
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."

    return inner


def parse_input(user_input):
    parts = user_input.strip().lower().split()
    cmd = parts[0] if parts else ""
    args = parts[1:]
    return cmd, args


@input_error
def hello_handler():
    return "How can I help you?"


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Usage: add <username> <phone>")

    username, phone = args
    contacts[username] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Usage: change <username> <phone>")

    username, phone = args

    if username not in contacts:
        raise KeyError(username)

    contacts[username] = phone
    return "Contact updated."


@input_error
def get_phone(args, contacts):
    username = args[0]

    if len(args) != 1:
        raise ValueError("Usage: phone <username>")

    return contacts[username]


@input_error
def get_all_contacts(contacts):
    if not contacts:
        return "No contacts found."

    return "\n".join(
        f"{name}: {phone}" for name, phone in contacts.items()
    )


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print(hello_handler())
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()