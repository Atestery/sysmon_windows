#pip install colorama
import colorama
colorama.init()
from termcolor import colored
#print(colored('hello', 'red'), colored('world', 'green'))
#print('\033[1;31mЭтот текст красный')
#print('\033[1;33mэтот желтый')
#print(colored('Hello World!', 'green'))
#print('\033[96mТекст будет голубым\033[0m')
#print("\x1b[31mТемно красный\x1b[0m")
#print('\033[0m а этот по умолчанию')

#pip3 install pygame
# для windows pip install  pygame
#pip install playsound
from playsound import playsound #для проигрывания звуков
from subprocess import PIPE, Popen
#import pygame # для воспроизведения звуков
import os  # Подкл библиотеку , можем выполнять команды в терминале,для определения ip
#import shutil #Для удаление каталога с файлами
import time
#import threading  # Потоки
import datetime  # определение времени и даты
#import smtplib  # для отправки почты
from datetime import datetime
import subprocess #для присвоение переменной результат команды system()
#import commands #для проверки даты создания последнего файла функция videosrv()

#os.system('clear') работает с linux. Если вы используете Windows, попробуйте os.system('CLS')


# Для определения погоды
# encoding=utf8
#import requests
#import html2text
#import sys

"""
hostname = "127.0.0.1"
nn = ' -n 1 '
ping_response = subprocess.Popen(['ping', hostname], stdout=subprocess.PIPE).stdout.read()
# Декодируем из байта в стринг
textcommand = ping_response.decode("cp866")
print(textcommand)

"""


def log(message):
    try:
        from datetime import datetime
        # Тут пишем код на проверку самой папки log
        # Проверяем если папка для лога есть пишем в нее, если ее нет то создаем ее и пишем в нее
        if os.path.exists('log\\'):
            # print("Проверка существования папки по пути:log")
            datein = datetime.strftime(datetime.now(), "%d_%m_%Y")
            file = open('log\\' + datein + '.log', "a")
            file.write("\n")
            file.write("\n")
            file.write("0-------------------------------------------0")
            file.write("\n")
            file.write(str(datetime.now()))
            file.write("\n")
            file.write(message)
            file.write("\n")
            file.write("1-------------------------------------------1")
            file.write("\n")
            file.write("\n")
            file.close()
        else:
            # Если такой папки нет то создаем ее и пишем в нее
            os.makedirs('log\\')  # Создаю такую папку и пишу в нее
            # print("Создал папку по пути: /home/pi/myprogramming/videoserver/log")
            datein = datetime.strftime(datetime.now(), "%d_%m_%Y")
            file = open('\log\\' + datein + '.log', 'a')
            file.write("\n")
            file.write("\n")
            file.write("0-------------------------------------------0")
            file.write("\n")
            file.write(str(datetime.now()))
            file.write("\n")
            file.write(message)
            file.write("\n")
            file.write("1-------------------------------------------1")
            file.write("\n")
            file.write("\n")
            file.close()
    except Exception as err:
        log("Сработало Исключение в функции log.")
        log(str(err))







print("Система мониторинга sysmon запущена!!!")
log("Система мониторинга sysmon запущена!!!")

try:
    while True:
        f = open('hosts.txt', 'r')
        # считываем построчно из файла
        spisok = [line.strip() for line in f]
        # print(l)
        f.close()
        # так можно определить длину массива
        dlinamas = len(spisok)
        # основной цикл считываем список ip из файла и пингуем
        for i in range(dlinamas):
            # разделяю строку по разделителю
            arr = spisok[i].split(';')
            # так могу вывести например только ip 1, днс 2
            hostname = arr[0]
            res = Popen("ping -n 1 " + hostname, shell=True, stdout=PIPE)
            out = str(res.communicate()[0].decode("CP866"))
            if out.find("100% потерь") != -1:
                #тут надо повторить пинг т.к. может ошибаться.
                res = Popen("ping -n 1 " + hostname, shell=True, stdout=PIPE)
                out = str(res.communicate()[0].decode("CP866"))
                if out.find("100% потерь") != -1:
                    # тут надо повторить пинг т.к. может ошибаться.
                    res = Popen("ping -n 1 " + hostname, shell=True, stdout=PIPE)
                    out = str(res.communicate()[0].decode("CP866"))
                    if out.find("100% потерь") != -1:
                        # тут надо повторить пинг т.к. может ошибаться.
                        res = Popen("ping -n 1 " + hostname, shell=True, stdout=PIPE)
                        out = str(res.communicate()[0].decode("CP866"))
                        if out.find("100% потерь") != -1:
                            print('\033[0m __________________________________________________________________')
                            print('\033[1;31mХост недоступен!!!: ', arr[0], arr[1], arr[2])
                            print('\033[0m __________________________________________________________________')
                            playsound('error_ping.mp3')
                            log('Хост недоступен!!!: ' + arr[0] + ' ' + arr[1] + ' ' + arr[2])
                #print('\033[0m __________________________________________________________________')
                #print('\033[1;31mХост недоступен!!!: ', arr[0], arr[1], arr[2])
                #print('\033[0m __________________________________________________________________')
                #playsound('error_ping.mp3')
                #log('Хост недоступен!!!: ' + arr[0] + ' ' + arr[1] + ' ' + arr[2])
            # else:
            # print("Хост недоступен!")

            # тут сделать проверку на миллисекунды Среднее = 0 мсек
            if out.find("Среднее = ") != -1:
                index = out.find("Среднее = ")
                index = index + 10
                responmc = ''
                while index != index + 10:
                    if out[index] != ' ':
                        responmc = responmc + out[index]
                    else:
                        break
                    index = index + 1
                responmc = int(responmc)
                if responmc > 1000:
                    print('\033[1;33m Внимание задержка пинга более 400мс ', arr[0], arr[1], arr[2])
                    playsound('err_time_ms.mp3')
                    log('Задержка пинга: ' + str(responmc) + ' ' + arr[0] + ' ' + arr[1] + ' ' + arr[2])
        time.sleep(60)
        os.system('CLS')
except Exception as err:
    print(str(err))
    print("Ошибка функции startping()")
    log("Ошибка функции startping() " + str(err))



log("Конец программы")







