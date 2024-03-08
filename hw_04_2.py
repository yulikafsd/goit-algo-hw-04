from pathlib import PurePath

dir_path = PurePath('__file__').parent

def get_cats_info(path):

    cats = []

    try:
        with open(path.joinpath('data', 'cats.txt'), 'r', encoding='utf-8') as fh:
            for line in fh.readlines():
                cat_data = line.strip().split(',')
                cats.append({'id': cat_data[0], 'name': cat_data[1], 'age': cat_data[2]})
    
    except FileNotFoundError:
        print('Вказаного файлу cats.txt не знайдено')
        return []
    
    for ind, cat in enumerate(cats):
        print(f'Кіт {ind+1}: {cat}')

    return cats

if __name__ == '__main__':
    get_cats_info(dir_path)