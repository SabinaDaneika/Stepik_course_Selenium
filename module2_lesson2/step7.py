# import os
#
# current_dir = os.path.abspath(os.path.dirname(__file__))
# # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')
# # добавляем к этому пути имя файла
# element.send_keys(file_path)

import os
from selenium import webdriver
from selenium.webdriver.common.by import By

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file_example.txt"
file_path = os.path.join(current_dir, file_name)
print(file_path)
