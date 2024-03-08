import sys
from pathlib import Path
from log import log_dir, log_error, log_file

def show_dir():

    try:

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

                    for item in directory.glob('**/*'):

                        # Розмічаємо файли та директорії різним форматуванням
                        if item.is_dir():
                            # Виводимо лише ім'я папки/файлу
                            log_dir(item.name)
                        else:
                            log_file(item.name)
                
                # Якщо шлях не веде до директорії, повідомляємо, що це файл
                else:
                    log_file(f'{directory.name} це файл')

            # Якщо такого шляху взагалі не існує, повідомляємо
            else:
                log_error(f'Директорії {directory.absolute()} не існує')
    
    except Exception as e:
            log_error(f'Помилка: {type(e).__name__} - {e}')

if __name__ == '__main__':
    show_dir()