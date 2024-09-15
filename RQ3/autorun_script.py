import os

import pyautogui as pag

def search_file(reg_exp, path):
    pag.hotkey('/')
    pag.sleep(1)
    pag.hotkey('ctrl', 'a')
    pag.sleep(0.5)
    pag.hotkey('backspace')
    pag.typewrite(reg_exp)
    pag.hotkey('enter')
    pag.sleep(15)
    pag.click()
    pag.sleep(0.3)
    pag.hotkey('ctrl', 'u')
    pag.sleep(15)
    pag.hotkey('ctrl', 's')
    pag.sleep(1)
    pag.typewrite(path)
    pag.sleep(1)
    pag.hotkey('enter')
    pag.sleep(1)
    pag.hotkey('ctrl', 'w')
    pag.sleep(1)

interval = "8_16"
path = f"reg_txt/{interval}.txt"
content = open(path,'r',encoding='utf-8',errors='ignore').readlines()
finish_results = os.listdir(f"temp/{interval}")

print("Runnning Program....")
pag.sleep(3)

for (i,c) in enumerate(content):
    while True:
        path = c.split('.java')[0]

        if f"{path}.html" in finish_results:
            print("finish")
            break
        reg_exp = c.split('.java')[1]
        reg_exp = reg_exp[1:len(reg_exp)]

        print(str(i) + " " + path)
        search_file(reg_exp,path)

        html_path = os.path.join(f"temp/{interval}", f"{path}.html")
        if os.path.exists(html_path):
            html_file = open(html_path,'r',encoding='utf-8')
            content = html_file.read().lower()
            html_file.close()
            break
        else:
            print(f"Error file : {path}")
            break