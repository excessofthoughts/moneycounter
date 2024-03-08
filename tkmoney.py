import tkinter as tk
from PIL import Image, ImageTk


def func1():
    res = 0
    for i in range(len(lis)):
        m = lis[i].get()
        if m == '':
            m = 0
        res += int(m) * noms[i]
    main_entry.delete(0, tk.END)
    main_entry.insert(0, str(res))


win = tk.Tk()
win.title('Moneycounter2024')
win.geometry('820x820')
win.config(bg='#2F4F4F')

noms = [1, 2, 5, 10, 50, 100, 200, 500, 1000, 2000, 5000]

img = Image.open('1.jpeg')
img = img.resize((125, 125))
imgg = ImageTk.PhotoImage(img)
label = tk.Label(win, image=imgg)
label.place(x=10, y=10)
entry1 = tk.Entry(win, width=13)
entry1.place(x=10, y=140)

img2 = Image.open('2.jpeg')
img2 = img2.resize((125, 125))
imgg2 = ImageTk.PhotoImage(img2)
label2 = tk.Label(win, image=imgg2)
label2.place(x=145, y=10)
entry2 = tk.Entry(win, width=13)
entry2.place(x=145, y=140)

img5 = Image.open('5.jpeg')
img5 = img5.resize((125, 125))
imgg5 = ImageTk.PhotoImage(img5)
label5 = tk.Label(win, image=imgg5)
label5.place(x=280, y=10)
entry5 = tk.Entry(win, width=13)
entry5.place(x=280, y=140)

img10 = Image.open('10.jpeg')
img10 = img10.resize((125, 125))
imgg10 = ImageTk.PhotoImage(img10)
label10 = tk.Label(win, image=imgg10)
label10.place(x=415, y=10)
entry10 = tk.Entry(win, width=13)
entry10.place(x=415, y=140)

img50 = Image.open('50.jpeg')
img50 = img50.resize((250, 125))
imgg50 = ImageTk.PhotoImage(img50)
label50 = tk.Label(win, image=imgg50)
label50.place(x=550, y=10)
entry50 = tk.Entry(win, width=27)
entry50.place(x=550, y=140)

img100 = Image.open('100.jpeg')
img100 = img100.resize((250, 125))
imgg100 = ImageTk.PhotoImage(img100)
label100 = tk.Label(win, image=imgg100)
label100.place(x=10, y=200)
entry100 = tk.Entry(win, width=27)
entry100.place(x=10, y=330)

img200 = Image.open('200.jpeg')
img200 = img200.resize((250, 125))
imgg200 = ImageTk.PhotoImage(img200)
label200 = tk.Label(win, image=imgg200)
label200.place(x=280, y=200)
entry200 = tk.Entry(win, width=27)
entry200.place(x=280, y=330)

img500 = Image.open('500.jpeg')
img500 = img500.resize((250, 125))
imgg500 = ImageTk.PhotoImage(img500)
label500 = tk.Label(win, image=imgg500)
label500.place(x=550, y=200)
entry500 = tk.Entry(win, width=27)
entry500.place(x=550, y=330)


img1000 = Image.open('1000.jpeg')
img1000 = img1000.resize((250, 125))
imgg1000 = ImageTk.PhotoImage(img1000)
label1000 = tk.Label(win, image=imgg1000)
label1000.place(x=10, y=400)
entry1000 = tk.Entry(win, width=27)
entry1000.place(x=10, y=530)


img2000 = Image.open('2000.jpeg')
img2000 = img2000.resize((250, 125))
imgg2000 = ImageTk.PhotoImage(img2000)
label2000 = tk.Label(win, image=imgg2000)
label2000.place(x=280, y=400)
entry2000 = tk.Entry(win, width=27)
entry2000.place(x=280, y=530)

img5000 = Image.open('5000.jpeg')
img5000 = img5000.resize((250, 125))
imgg5000 = ImageTk.PhotoImage(img5000)
label5000 = tk.Label(win, image=imgg5000)
label5000.place(x=550, y=400)
entry5000 = tk.Entry(win, width=27)
entry5000.place(x=550, y=530)

label_task = tk.Label(win ,text='Введите количество монет или купюр  каждого номинала и нажмите на кнопку, чтобы посчитать сумму', fg='white', bg='#2F4F4F')
label_task.place(x=45, y=600)

main_entry = tk.Entry(win, width=87, fg='red')
main_entry.place(x=10, y=650)

lis = [entry1, entry2, entry5, entry10, entry50, entry100, entry200, entry500, entry1000, entry2000, entry5000]

baton = tk.Button(win, text='Посчитать!', command=func1)
baton.place(x=355, y=700)

win.mainloop()
