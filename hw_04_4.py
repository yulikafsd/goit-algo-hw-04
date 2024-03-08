def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):

    # Обробка ValueError якщо аргс менше ніж має бути ----------------------!

    name, phone = args

    # якщо контакта з таким ім'ям немає, записати
    if contacts.get(name) == None:
        contacts[name] = phone
        return "Contact added."
    
    # якщо контакт з таким ім'ям вже є, перепитати
    else:
        user_input = input("A contact with this name already exists.\nDo you really want to change this contact? Y/N: ")
        if user_input.lower() == 'y':
            contacts[name] = phone
            return "Contact changed."
        else:
            return "Contact was not changed."

def change_contact(args, contacts):

    # Обробка ValueError якщо аргс менше ніж має бути ----------------------!

    name, phone = args

    # Повідомлення про помилку, якщо ім'я не знайдено
    if contacts.get(name) == None:
        user_input=input("Contact with this name was not found. Add a new contact? Y/N: ")
        if user_input.lower() == 'y':
            contacts[name] = phone
            return "Contact added."
        else:
            return "Contact was not added."

    else:
        contacts[name] = phone
        return "Contact was changed."

def show_phone(args, contacts):
    
    # Обробка IndexError або довжина аргс, якщо аргс менше ніж має бути -------!

    name = args[0]

    # Повідомлення про помилку, якщо ім'я не знайдено
    if contacts.get(name) == None:
        return "Contact with this name was not found"
    # Вивід: [номер телефону]
    else:
        return contacts[name]

def show_all(contacts):
    
    if len(contacts) == 0:
        return "Контактів не знайдено"
    
    for key, value in contacts.items():
        return(f"{key}: {value}")

def main():
    contacts = {}

    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break

            case "hello":
                print("How can I help you?")

            case "add":
                print(add_contact(args, contacts))

            case "change":
                print(change_contact(args,contacts))

            case "phone":
                print(show_phone(args, contacts))
        
            case "all":
                print(show_all(contacts))

            case _:
                print("Invalid command.")
                
if __name__ == "__main__":
    main()