from pathlib import Path

def total_salary(path):

    if not path.exists():
        print('Вказаний файл не знайдено')
        return None
    
    if not path.is_file():
        print('Вказаний шлях веде не до файлу')
        return None
    
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            total = 0
            workers = 0
            
            for ind, line in enumerate(fh, start=1):
                try:
                    _, value = line.strip().split(',')
                    if value.isdigit():
                        total += int(value)
                        workers += 1
                    else:
                        raise ValueError
                
                except ValueError:
                    print(f'Неправильне значення зарплати у рядку {ind}')
                    return None
            
            if workers == 0:
                print('Файл порожній')
                return None
            
            average = total // workers
            print(f"Для {workers} робітників загальна сума заробітної плати: {total}, середня заробітна плата: {average}")
            return [total, average]
    
    except FileNotFoundError:
        print('Вказаного файлу не знайдено')
        return None

if __name__ == '__main__':
    dir_path = Path('data/salaries.txt')
    total_salary(dir_path)