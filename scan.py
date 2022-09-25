from audioop import add
from email.mime import image
import requests
import hashlib
from inspect import signature
import time
from tkinter import *
from tkinter.filedialog import askopenfilename
import pprint

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
    #print (file_signature)
    return file_signature
#s = scan('C:/Users/p_k12/test1/dist/One.exe')
#print (s)
def compare(one,two,name,list_dict_compare_2):
    two = two[0]
    #print (two)
    len = 0
    for item_one in one:
        len += 1
    interest = 100/len
    #interest = int(interest)
    #print ("1 совпадение - " + str(interest) + " %")
    interests = 0
    for item in one:
        for item2 in two:
            if (item == item2):
                interests += interest
                break
    dict_compare_2 = dict.fromkeys([name],[interests])
    list_dict_compare_2.append(dict_compare_2)
    #print (dict_compare_2)
    #print (interests)
    return list_dict_compare_2  

#c = compare(s,virus_signature)
#print ("Совпадение сигнатур : " + str(c) + " %")

def clicked():
    skan_virus_name = ["virus_1","virus_2","virus_3","virus_4"]
    lbox.insert(0,'')
    list_dict_compare_2 = []
    op = askopenfilename()  
    for item in signature_dict:
        #print ("____________________________________")
        #print (item)
        #print (item[skan_virus_name[0]])
        #print (skan_virus_name[0])
        s = scan(op)
        c = compare(s,item[skan_virus_name[0]],skan_virus_name[0],list_dict_compare_2)
        del skan_virus_name[0]
        key = item.values()
        #key = key[0]
    #print (c)
    for item in c:
        for key, value in item.items():
            for item2 in item[key]:
                #item3 = item2
                txt = "Совпадение с {0} - {1} %".format(key,item2)
                if (float(item2) > 0):
                    txt = "Совпадение с {0} - {1} %  ---!".format(key,item2)
            #print("{0}: {1}".format(key,value))
            #print (item)
            #lb2.configure(text=item)
                #--|
                lbox.insert(0,txt)
    #if (c > 50):  
    #    lb2.configure(text=c)
    #    lb3.configure(text="Высокая вероятность вируса")

 
window = Tk() 
photo_2 = PhotoImage(file= r"C:\Users\p_k12\test1\dist\stick.png")
photo_3 = PhotoImage(file= r"C:\Users\p_k12\test1\dist\town.png")
window.geometry('556x700')
window.configure(bg='black')
window.title("")
#baclground_label = Label(image=photo_3, bd = 0)
#baclground_label.place(x=0,y=0,relwidth=1,relheight=1)
def motion_car_1():
    
    if int(c.coords(car_1)[0]) < 700 :
        c.move(car_1, -1.3, 0)
        window.after(10, motion_car_1)
    if int(c.coords(car_1)[0] < 0):
        c.move(car_1, 600, 0)
def motion_car_2(): 
    if  int(c.coords(car_2)[0]) < 700 :
        c.move(car_2, -1, 0)
        window.after(10, motion_car_2)
    if int(c.coords(car_2)[0]) < 0:
        c.move(car_2, 650, 0)
def motion_car_3():
    if  int(c.coords(car_3)[0]) < 700:
        c.move(car_3, 1,0)
        window.after(10, motion_car_3)
    if int(c.coords(car_3)[0]) > 610:
        c.move(car_3, -700,0)

c = Canvas(window, width=550, height=464, bd = 0,
           bg="black")
           
c.grid(column=0,row=5)
lbl = Label(window, text="Samurai", font=("Inter", 20), bg = 'black')
lbl.grid(column=0, row=0) 
lbox = Listbox(width=50,height=5, bg = 'lightgray', bd = 0)
lbox.grid(column=0,row=1)
lbl_1 = Label(window, text="Samurai", font=("Inter", 20), bg = 'black')
lbl_1.grid(column=0, row=2) 
btn1 = Button(window, text="Открыть файл", font=("Iter",15),command=clicked, bg = 'lightgray', bd = 0, activebackground = 'lightgray')
btn1.grid(column=0,row=3)
lbl_2 = Label(window, text="Samurai", font=("Inter", 20), bg = 'black')
lbl_2.grid(column=0, row=4) 
photo_car_1 = PhotoImage(file = r"C:\Users\p_k12\test1\dist\car_1.png")
photo_car_2 = PhotoImage(file = r"C:\Users\p_k12\test1\dist\car_2.png")
photo_car_3 = PhotoImage(file = r"C:\Users\p_k12\test1\dist\car_3.png")
c.create_image(0,0,anchor=NW, image=photo_3)
car_1 = c.create_image(620,445, anchor=SE,image=photo_car_1 )
car_2 = c.create_image(650,455, anchor=SE,image=photo_car_2 )
car_3 = c.create_image(-50,465, anchor=SE,image=photo_car_3 )
#btn1 = Button(window, text="Открыть файл", font=("Iter",15),command=motion_car_1, bg = 'lightgray', bd = 0, activebackground = 'lightgray')
#btn1.grid(column=10,row=4)
#lbl = Label(window, text="Samurai", font=("Inter", 50), bg = 'lightgray')
#lbl.grid(column=0, row=0)  
#lb2 = Label(window, text="",font=("Iter",20), bg = 'lightgray')
#lb2.grid(column=0,row=2)
#lb3 = Label(window,text="", font=("Iter",20), bg = 'lightgray',image=photo_2)
#lb3.grid(column=6,row=4)
motion_car_1()
motion_car_2()
motion_car_3()
window.mainloop()
