import tkinter
import time
from tkinter import filedialog,messagebox
import requests
from sys import exit
from playsound import playsound
# 选取文件
root = tkinter.Tk()
rewrite_menu = True
path = filedialog.askopenfilename()
messagebox.showwarning('提示','正在进行电子签名验证,请确保文件为xie语言文件')
messagebox.askquestion('提示','是否继续加载文件')
root.withdraw()
if path.split('/')[-1].split('.')[-1] == 'xie':
    messagebox.showinfo('提示','文件已加载')
    with open(path, 'r',encoding='utf-8') as filedata:

        linesList= filedata.readlines()

        #从行列表中删除新行字符（\n）
        xie_t = [k.rstrip('\n') for k in linesList]

    # 处理
    for i in xie_t:
        '''
        1.0b添加
        '''
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

        '''
        2.0b 添加
        '''
        if i.split('>>')[0] == 'time':
            time.sleep(int(i.split('>>')[1]))
        # flask 模块
        if i.split('>>')[0]=='audio.play':
            playsound(i.split('>>')[1])
    time.sleep(2)
else:
    messagebox.showerror('error','未通过电子签名验证')