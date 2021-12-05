"""Создайте функции, одна из которых читает файл на диске с заданным именем и проверяет наличие строку “Wow! ”.
В случае, если файла нет, то засыпает на 5 секунд, а затем снова продолжает поиск по файлу. В случае, если 
файл есть, то открывает его и ищет строку “Wow!”. При наличии данной строки закрывает файл и генерирует событие,
а другая функция ожидает  данное событие и в случае его возникновения выполняет удаление этого файла. В случае если 
строки «Wow!» не было найдено в файле, то засыпать на 5 секунд. Создайте файл руками и проверьте выполнение программы."""

import os
import os.path
from time import sleep
import asyncio
import re

file_name = 'find_wow.txt'


async def find_file():
    cur_dir = os.getcwd()
    while True:
        file_list = os.listdir(cur_dir)
        parent_dir = os.path.dirname(cur_dir)
        if file_name in file_list:
            input_file = open(file_name, mode='r', encoding='utf-8')
            my_text = input_file.read()
            if re.findall(r'(?im)wow!', my_text):
                print('"Wow!" has found!')
                break
            else:
                print('Going to sleep for 5 sec and start to find test ( "Wow!" ) one more time!')
                sleep(5)
        else:
            if cur_dir == parent_dir:
                print('Going to sleep for 5 sec and start to find "find_wow.txt" one more time!')
                sleep(5)
            else:
                cur_dir = parent_dir


async def delete_file():
    try:
        os.remove(file_name)
        print('File has been removing!')
    except OSError:
        print('Error')


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
tasks = asyncio.wait([
    loop.create_task(find_file()),
    loop.create_task(delete_file())
])
loop.run_until_complete(tasks)
