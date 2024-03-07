from pathlib import PurePath

dir_path = PurePath('__file__').parent

def get_cats_info(path):

    cats = list()

    try:
        with open(f'{path}/data/cats.txt', 'r', encoding='utf-8') as fh:
            for line in fh.readlines():
                cat_data = line.strip().split(',')
                cats.append({'id': cat_data[0], 'name': cat_data[1], 'age': cat_data[2]})
    
    except FileNotFoundError:
        print('Вказаного файлу cats.txt не знайдено')
    
    print(f'Наші коти:\n{cats[0]}\n{cats[1]}\n{cats[2]}\n{cats[3]}\n{cats[4]}')
    return cats

if __name__ == '__main__':
    get_cats_info(dir_path)