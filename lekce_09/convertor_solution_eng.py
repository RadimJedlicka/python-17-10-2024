import os
from pprint import pprint

def start_translation(file: str, dictionary: dict):
    if os.path.isfile(file):
        print('Starting translation')
        bytes_data = read_txt_file(file)
        new_data = iterate_through_all_data(bytes_data, dictionary)
        pprint(new_data)
    else:
        print('File does not exist')

def read_txt_file(file: str) -> list:
    with open(file, mode='r', encoding='UTF-8') as txt:
        return txt.readlines()

def iterate_through_all_data(data: list, dictionary: dict) -> list:
    '''
    If you return a list in the return statement, the list will be printed in the same order as iterated.
    If you return a set (using {}), values will be sorted in descending order.
    '''
    return [
        rewrite_new_byte_type(detail, dictionary) 
        for detail in data
    ]

def rewrite_new_byte_type(detail: str, dictionary: dict) -> str:
    '''
    Be careful when adding values from dictionaries using keys (using the .get method):
    If the key is not found, the program will end with an error (as in the penultimate line of our file,
    where it is "byt0008").
    However, we can handle this using the second argument of the .get method,
    where we write a string that will be added in case the key was not found.
    '''
    disposition, *rest = detail.split(',', maxsplit=1)
    new_entry = dictionary.get(disposition, 'Unknown position')
    return ', '.join((new_entry, ', '.join(rest)))

def apartment_translation():
    abs_path = f'{os.getcwd()}{os.sep}solution{os.sep}input_data.txt'

    translation_pattern = {
        "byt0001": "1+1",
        "byt0002": "2+1",
        "byt0003": "2+kk",
        "byt0004": "3+1",
        "byt0005": "3+kk",
        "byt0006": "4+1",
        "byt0007": "4+kk",
    }

    start_translation(abs_path, translation_pattern)

if __name__ == '__main__':
    apartment_translation()
