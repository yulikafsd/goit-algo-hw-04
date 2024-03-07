import sys
from pathlib import Path
from log import log_dir, log_error, log_file

def show_dir():

    # Перевіряємо, чи було введено аргумент
    if len(sys.argv) <= 1:
        log_error('Шлях не вказаний')
        return
    
    # Створюємо шлях
    else:
        directory = Path(sys.argv[1])
        
        # Перевірка, чи існує такий шлях
        if directory.exists():
            
            # Якщо шлях це директорія, ітеруємо її зміст
            if directory.is_dir():
                print(f'Знайдено директорію {directory}:')
                # items = directory.iterdir()
                items = directory.glob('**/*')

                for item in items:
                    
                    # Видобуваємо зі шляху лише назву файлу або директорії 
                    item_name = str(item).split('\\')
                    name_ind = len(item_name) - 1

                    # Розмічаємо файли та директорії різним форматуванням
                    if item.is_dir():
                        log_dir(item_name[name_ind])
                    else:
                        log_file(item_name[name_ind])
            
            # Якщо шлях не веде до директорії, повідомляємо, що це файл
            else:
                log_file(f'{directory} це файл')

        # Якщо такого шляху взагалі не існує, повідомляємо
        else:
            log_error(f'Директорії {directory.absolute()} не існує')

if __name__ == '__main__':
    show_dir()