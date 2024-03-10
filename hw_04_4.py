def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name.lower()] = phone
    return f"Contact {name.capitalize()} with phone {phone} added."

def change_contact(args, contacts):
    name, phone = args
    contacts[name.lower()] = phone
    return f"{name.capitalize()}'s phone changed to: {phone}."

def show_phone(args, contacts):
    name = args[0]

    # Повідомлення про помилку, якщо ім'я не знайдено
    if contacts.get(name.lower()) == None:
        return f"Contact with name {name.capitalize()} was not found"
    
    else:
        # Якщо знайдено, вивід: [номер телефону]
        return contacts[name.lower()]

def show_all(contacts):
    
    if len(contacts) == 0:
        return "No contacts were found"
    
    print(contacts)
    contacts_string = ""
    for key, value in contacts.items():
        # тут простіше було б зробити одразу print кожного контакту, 
        # але за умовами ДЗ всі print мають бути в main, тому:
        contacts_string += f"\n{key.capitalize()}: {value}" 
    return f"Your contacts: {contacts_string}"

def main():
    contacts = {}

    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        
        try:
            command, *args = parse_input(user_input)

            match command:
                case "close" | "exit":
                    print("Good bye!")
                    break

                case "hello":
                    print("How can I help you?")

                case "add":
                    try:
                        # якщо контакта з таким ім'ям немає, записати
                        if contacts.get(args[0].lower()) == None:
                            print(add_contact(args, contacts))
                        
                        # якщо контакт з таким ім'ям вже є, перепитати
                        else:
                            user_input = input("Contact with this name already exists.\nChange this contact? Y/N: ")
                            if user_input.lower() == 'y':
                                print(change_contact(args, contacts))
                            else:
                                print("Contact was not changed.")
                    
                    # Обробка винятка, якщо аргс менше ніж має бути
                    except Exception as e:
                        print(f"Wrong format. Please, enter: add [contact_name] [phone_number]. Error - {e}")

                case "change":
                    try:               
                        # Якщо ім'я не знайдено, пропонуємо додати
                        if contacts.get(args[0].lower()) == None:
                            user_input = input("Contact with this name was not found.\nAdd a new contact? Y/N: ")
                            if user_input.lower() == 'y':
                                print(add_contact(args,contacts))
                            else:
                                print("Contact was not added.")

                        else:
                            print(change_contact(args,contacts))
                    
                    # Обробка винятка, якщо аргс менше ніж має бути
                    except Exception as e:
                        print(f"Wrong format. Please, enter: change [contact_name]. Error - {e}")

                case "phone":
                    try:
                        print(show_phone(args, contacts))
                    
                    # Обробка винятка, якщо аргс менше ніж має бути
                    except Exception as e:
                        print(f"Wrong format. Please, enter: phone [contact_name]. Error - {e}")
            
                case "all":
                    print(show_all(contacts))

                case _:
                    print("Invalid command.")
        
        except Exception as e:
            print(f"No command entered. Error - {e}")

if __name__ == "__main__":
    main()