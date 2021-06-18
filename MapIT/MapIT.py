#! Python
# Программа, которая открывает карты в браузере, 
# извлекая адрес из командной строки или буфера обмена

# подключение необходимых библиотек
import webbrowser
import sys
import pyperclip
import pyperclip


if(len(sys.argv) > 1):
    # получение адреса из командной строки
    adress = " ".join(sys.argv[1:])
else:
    # получение адреса из буфера обмена
    adress = pyperclip.paste()

print("GoogleMaps запущены с адресом " + adress + "...")

# открытие карты
webbrowser.open("https://www.google.com/maps/place/" + adress)