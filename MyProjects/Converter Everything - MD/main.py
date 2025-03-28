# import pypandoc
import pathlib

# output = pypandoc.convert_text('<h1>Hello, Markdown!</h1>', 'md', format='html')
# print(output)

# Импортируем необходимые библиотеки
from pypandoc import convert_file
from pathlib import Path
import os

# Объявляем функцию для конвертации файлов
def convert_to_md(input_file, output_file):
    try:
        # Проверяем расширение входного файла
        if not input_file.lower().endswith('.md'):
            raise ValueError("Указанный файл не является файлом Markdown.")

        # Проверяем существование входного файла
        if not os.path.exists(input_file):
            raise FileNotFoundError("Указанный файл не найден.")

        # Конвертируем файл в Markdown
        convert_file(input_file, 'md', outputfile=output_file)

        # Выводим сообщение об успешной конвертации
        print(f"Конвертация файла {input_file} в Markdown успешно завершена.")
    except (ValueError, FileNotFoundError) as e:
        print(f"Ошибка: {e}")

# Пример использования функции

def get_all_files(directory: str):
    """Get all files from a directory."""

    file_list = pathlib.Path(directory).glob('**/*')
    file_paths = [str(file) for file in file_list]
    print(file_paths)


FILE_STORE_PATH = 'file_store'
get_all_files(FILE_STORE_PATH)


# input_file = Path.
# output_file = "output.md"
# convert_to_md(input_file, output_file)