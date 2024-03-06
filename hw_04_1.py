from pathlib import PurePath

path = PurePath(__file__).parent

def total_salary(path):
    
    try:
        with open(f'{path}/salaries.txt', 'r', encoding='utf-8') as fh:
            total = 0
            workers = 0
            
            for item in fh.readlines():
                _, value = item.strip().split(',')
                total += int(value)
                workers += 1
            
            average = total // workers
            print(f"Для {workers} робітників загальна сума заробітної плати: {total}, середня заробітна плата: {average}")
            return [total, average]
    
    except FileNotFoundError:
        print('Вказаного файлу salaries.txt не знайдено')

    except ValueError:
        print('Значення заробітної плати не є числом')

if __name__ == '__main__':
    total_salary(path)