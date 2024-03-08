from pathlib import Path

def get_cats_info(path):

    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as fh:
            for ind, line in enumerate(fh):
                cat_data = line.strip().split(',')
                cat = {'id': cat_data[0], 'name': cat_data[1], 'age': cat_data[2]}
                cats.append(cat)
                print(f'Кіт {ind}: {cat}')
        return cats
    
    except FileNotFoundError:
        print('Вказаного файлу cats.txt не знайдено')
        return []

if __name__ == '__main__':
    dir_path = Path('data/cats.txt')
    get_cats_info(dir_path)