import tkinter
import time
from tkinter import filedialog,messagebox
import requests
# 选取文件
root = tkinter.Tk()
path = filedialog.askopenfilename()
rewrite_menu = True
root.withdraw()

with open(path, 'r',encoding='utf-8') as filedata:

    linesList= filedata.readlines()

    #从行列表中删除新行字符（\n）
    xie_t = [k.rstrip('\n') for k in linesList]

# 处理
for i in xie_t:
    if i.split('>>')[0] == 'print':
        if len(i.split('>>')) == 2:
            print(i.split('>>')[1])
        elif len(i.split('>>')) == 3:
            num = int(i.split('>>')[2])
            for j in range(num):
                print(str(i.split('>>')[1]))
    elif i.split('>>')[0] == 'input':
        if len(i.split('>>')) == 2:
            input(i.split('>>')[1])
        elif len(i.split('>>')) == 3:
            a = input(i.split('>>')[1])
    # requests 模块
    elif i.split('>>')[0] == 'requests.get':
        url = i.split('>>')[1]
        type = i.split('>>')[2]
        if type == 'text':
            print(requests.get(url).text)
        elif type == 'cookie':
            print(requests.get(url).cookies)
        elif type == 'code':
            print(requests.get(url).status_code)
time.sleep(5)