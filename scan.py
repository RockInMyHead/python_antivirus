from audioop import add
import requests
import hashlib
from inspect import signature
import time
from tkinter import *
from tkinter.filedialog import askopenfilename

#from * import signatyre
import signatyre

signature_dict = signatyre.create_signature() # сигнатрура вирусов
#print (signature_dict)
skan_virus_name = ["virus_1","virus_2","virus_3","virus_4"]

def scan(path):
    with open (path, "rb") as f:
        bytes = f.read()
    new_bytes = str(bytes).replace('\\x','')
    new_bytes = new_bytes.replace(' ','')
    len = 0
    a = 0
    file_signature = []
    my_iteration = 0
    for item in new_bytes: # Считаем колличесвто символов
        len+=1
    #print ("Элементов: " + str(len))
    iteration = len / 32768 # Считаем колличество блоков по 512 знаков
    iteration = int(iteration) + 1 # Округляем, +1 для округления в большую сторону
    #print ("Колличество реальных итераций: " + str(iteration))
    while my_iteration < iteration:
        a+=1
        #print (a)
        first_pack = "".join(new_bytes[:32768])
        new_bytes = new_bytes[32768:]
        md5hash = hashlib.md5(first_pack.encode())
        md5hash_hexdigest = md5hash.hexdigest()
        #print (md5hash.hexdigest())
        my_iteration += 1
        file_signature.append(md5hash_hexdigest)
    #print (first_pack)
    print (file_signature)
    return file_signature
#s = scan('C:/Users/p_k12/test1/dist/One.exe')
#print (s)
def compare(one,two,name,list_dict_compare_2):
    two = two[0]
    print (two)
    len = 0
    for item_one in one:
        len += 1
    interest = 100/len
    #interest = int(interest)
    print ("1 совпадение - " + str(interest) + " %")
    interests = 0
    for item in one:
        for item2 in two:
            if (item == item2):
                interests += interest
                break
    dict_compare_2 = dict.fromkeys([name],[interests])
    list_dict_compare_2.append(dict_compare_2)
    print (dict_compare_2)
    #print (interests)
    return list_dict_compare_2  

#c = compare(s,virus_signature)
#print ("Совпадение сигнатур : " + str(c) + " %")

def clicked():
    list_dict_compare_2 = []
    op = askopenfilename()  
    for item in signature_dict:
        print ("____________________________________")
        #print (item)
        #print (item[skan_virus_name[0]])
        print (skan_virus_name[0])
        s = scan(op)
        c = compare(s,item[skan_virus_name[0]],skan_virus_name[0],list_dict_compare_2)
        del skan_virus_name[0]
        key = item.values()
        #key = key[0]
    print (c)
    for item in c:
        #print (item)
        #lb2.configure(text=item)
        lbox.insert(0,item)
        time.sleep(2)
    #if (c > 50):  
    #    lb2.configure(text=c)
    #    lb3.configure(text="Высокая вероятность вируса")

window = Tk()  
window.geometry('700x450')
window.title("")
lbox = Listbox(width=40,height=40)
lbox.grid(column=0,row=7)
lbl = Label(window, text="", font=("Inter", 50))
lbl.grid(column=0, row=0)  
lb2 = Label(window, text="",font=("Iter",20))
lb2.grid(column=0,row=2)
lb3 = Label(window,text="", font=("Iter",20))
lb3.grid(column=0,row=4)
btn1 = Button(window, text="Открыть файл", command=clicked)
btn1.grid(column=1,row=0)
window.mainloop()