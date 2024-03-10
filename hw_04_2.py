from pathlib import Path

def get_cats_info(path):

    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as fh:
            for ind, line in enumerate(fh):
                cat_id, cat_name, cat_age = line.strip().split(',')
                cat = {'id': cat_id, 'name': cat_name, 'age': cat_age}
                cats.append(cat)
                print(f'Кіт {ind}: {cat}')
        return cats
    
    except FileNotFoundError:
        print('Вказаного файлу cats.txt не знайдено')
        return []

if __name__ == '__main__':
    dir_path = Path('data/cats.txt')
    get_cats_info(dir_path)