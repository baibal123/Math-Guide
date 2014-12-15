"""Math-Guide the project"""
import sys
from Tkinter import *
import tkMessageBox

def homepagedef():
    """homepage of the program"""
    global homepage
    homepage = Tk()
    homepage.geometry('450x350')
    photo = PhotoImage(file="Teammy.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Button1 = Button(text ="Chapter 1 - Set", command = chapter1 , fg = 'black', bg = 'yellow', height = 2, width = 63).grid(row =1, column =0, sticky = W)
    Button2 = Button(text ="Chapter 2 - Logic", command = chapter2 , fg = 'black', bg = 'yellow', height = 2, width = 63).grid(row =2, column =0, sticky = W)
    Button3 = Button(text ="Chapter 3 - Reasoning", command = chapter3 , fg = 'black', bg = 'yellow', height = 2, width = 63).grid(row =3, column =0, sticky = W)
    Button4 = Button(text ="Chapter 4 - propositional logic", command = donothing , fg = 'black', bg = 'yellow', height = 2, width = 63).grid(row =4, column =0, sticky = W)
    Button5 = Button(text ="Chapter 5 - propositional logic", command = donothing , fg = 'black', bg = 'yellow', height = 2, width = 63).grid(row =5, column =0, sticky = W)
    texti = Label(text = 'test-->Chapter', fg = 'yellow', bg = 'black', height = 3, width = 20).grid(row =6, column =0, sticky = W)
    Buttont1 = Button(text ="1", command = test1page1gui , fg = 'yellow', bg = 'black', height = 3, width = 5).place(x = 146, y = 298)
    Buttont2 = Button(text ="2", command = test2page1gui , fg = 'yellow', bg = 'black', height = 3, width = 5).place(x = 191, y = 298)
    Buttont3 = Button(text ="3", command = test3page1gui , fg = 'yellow', bg = 'black', height = 3, width = 5).place(x = 236, y = 298)
    Buttont4 = Button(text ="4", command = donothing , fg = 'yellow', bg = 'black', height = 3, width = 5).place(x = 281, y = 298)
    Buttont5 = Button(text ="5", command = donothing , fg = 'yellow', bg = 'black', height = 3, width = 5).place(x = 326, y = 298)
    Buttont6 = Button(text ="Final", command = donothing , fg = 'yellow', bg = 'black', height = 3, width = 10).place(x = 371, y = 298)

    menubar = Menu(homepage)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command = closehomepage)
    menubar.add_cascade(label = "File", menu = filemenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_separator()
    helpmenu.add_command(label="Credits", command = credit)
    menubar.add_cascade(label = "Help", menu = helpmenu)

    homepage.config(menu=menubar)
    homepage.mainloop()
    
def donothing():
    """use for testing program"""
    pass

def credit():
    """Credits Box"""
    tkMessageBox.showinfo("Credits", "Math-Guide V.1.0 create by baibal123(57070040)")

def closehomepage():
    """Menu-->Exit the program"""
    exits = tkMessageBox.askyesno('Exit', 'Are you sure?')
    if exits > 0:
        homepage.destroy()

def chapter1():
    """Chapter one recreate new window"""
    homepage.destroy()
    global set_page
    set_page = Tk()
    set_page.geometry('875x600')
    photo = PhotoImage(file="Set_page1.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    menubar = Menu(set_page)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command = close_set)
    menubar.add_cascade(label = "File", menu = filemenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Instuction")
    helpmenu.add_separator()
    helpmenu.add_command(label="Credits", command = credit)
    menubar.add_cascade(label = "Help", menu = helpmenu)
    set_page.config(menu=menubar)
    Buttont1 = Button(text ="Next", command = chapter1page2 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 750, y = 498)

def close_set():
    """Exit the program while in chapter"""
    exits = tkMessageBox.askyesno('Exit', 'Are you sure?')
    if exits > 0:
        set_page.destroy()

def chapter1page2():
    """once of page"""
    photo = PhotoImage(file="Set_page2.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter1page3 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 750, y = 498)

def chapter1page3():
    """once of page"""
    photo = PhotoImage(file="Set_page3.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter1page4 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 750, y = 498)

def chapter1page4():
    """once of page"""
    photo = PhotoImage(file="Set_page4.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter1page5 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 750, y = 498)
    
def chapter1page5():
    """once of page"""
    photo = PhotoImage(file="Set_page5.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter1page6 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 750, y = 498)

def chapter1page6():
    """once of page"""
    photo = PhotoImage(file="Set_page6.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter1page7 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 750, y = 498)

def chapter1page7():
    """once of page"""
    photo = PhotoImage(file="Set_page7.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = test1page1 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 750, y = 498)

def test1page1():
    """page for test"""
    photo = PhotoImage(file="Set_quiz1.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="1.", command = wrong , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 540, y = 165)
    Buttont2 = Button(text ="2.", command = wrong , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 540, y = 229)
    Buttont3 = Button(text ="3.", command = correct , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 540, y = 295)
    Buttont4 = Button(text ="4.", command = wrong , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 540, y = 364)

def test2page1gui():
    """test chap2 page1 run from interface"""
    homepage.destroy()
    global set_page
    set_page = Tk()
    set_page.geometry('875x600')
    photo = PhotoImage(file="logic_quiz1.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Yes", command = correct3 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 110, y = 60)
    Buttont2 = Button(text ="No", command = wrong , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 180, y = 60)
    Buttont3 = Button(text ="Yes", command = correct3 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 110, y = 155)
    Buttont4 = Button(text ="No", command = wrong , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 180, y = 155)
    Buttont5 = Button(text ="Yes", command = correct3 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 110, y = 253)
    Buttont6 = Button(text ="No", command = wrong , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 180, y = 253)
    Buttont7 = Button(text ="Yes", command = wrong , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 110, y = 348)
    Buttont8 = Button(text ="No", command = correct3 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 180, y = 348)
    Buttont9 = Button(text ="Yes", command = wrong , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 110, y = 440)
    Buttont10 = Button(text ="No", command = correct3 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 180, y = 440)
    Buttont11 = Button(text ="Yes", command = correct3 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 110, y = 535)
    Buttont12 = Button(text ="No", command = wrong , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 180, y = 535)
    Buttont13 = Button(text ="Next", command = ans_page3 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 775, y = 550)

def test1page1gui():
    """test page but run from interface"""
    homepage.destroy()
    global set_page
    set_page = Tk()
    set_page.geometry('875x600')
    photo = PhotoImage(file="Set_quiz1.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="1.", command = wrong , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 540, y = 165)
    Buttont2 = Button(text ="2.", command = wrong , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 540, y = 229)
    Buttont3 = Button(text ="3.", command = correct , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 540, y = 295)
    Buttont4 = Button(text ="4.", command = wrong , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 540, y = 364)
    menubar = Menu(set_page)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command = close_set)
    menubar.add_cascade(label = "File", menu = filemenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Instuction")
    helpmenu.add_separator()
    helpmenu.add_command(label="Credits", command = credit)
    menubar.add_cascade(label = "Help", menu = helpmenu)
    set_page.config(menu=menubar)

def test3page1gui():
    """test chap3 page1 run from interface"""
    homepage.destroy()
    global set_page
    set_page = Tk()
    set_page.geometry('875x600')
    photo = PhotoImage(file="reason_quiz1.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    global dummy
    dummy = StringVar()
    global dummy2
    dummy2 = StringVar()
    dummy.set('answer here')
    dummy2.set('answer here')
    mntry = Entry(set_page, textvariable = dummy, fg = 'black', bg = 'yellow').place(x = 115, y = 330)
    mntry2 = Entry(set_page, textvariable = dummy2, fg = 'black', bg = 'yellow').place(x = 115, y = 430)
    Buttontx1 = Button(text ="commit", command = commit_ans , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)


def correct():
    """Correct box for reply the correct answer"""
    tkMessageBox.showinfo("Answer", "Correct!!")
    ans_page1()
    
def test1page2():
    """test set page2"""
    photo = PhotoImage(file="Set_quiz2.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="1.", command = wrong , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 540, y = 265)
    Buttont2 = Button(text ="2.", command = wrong , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 540, y = 329)
    Buttont3 = Button(text ="3.", command = correct2 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 540, y = 395)
    Buttont4 = Button(text ="4.", command = wrong , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 540, y = 464)

def correct2():
    """correct box for page two"""
    tkMessageBox.showinfo("Answer", "Correct!!")
    ans_page2()

def ans_page1():
    """Solver page1"""
    photo = PhotoImage(file="Set_quiz1ans.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = test1page2 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 750, y = 498)

def ans_page2():
    """Solver page2"""
    photo = PhotoImage(file="Set_quiz2ans.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = back , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 750, y = 498)

def back():
    """back to homepage"""
    set_page.destroy()
    homepagedef()

def wrong():
    """wrong box reply for wrong answer"""
    tkMessageBox.showinfo("Answer", "Nice Try but it's wrong!!")

def chapter2():
    """Chapter2 homepage"""
    homepage.destroy()
    global set_page
    set_page = Tk()
    set_page.geometry('875x600')
    photo = PhotoImage(file="logic1.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    menubar = Menu(set_page)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command = close_set)
    menubar.add_cascade(label = "File", menu = filemenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Instuction")
    helpmenu.add_separator()
    helpmenu.add_command(label="Credits", command = credit)
    menubar.add_cascade(label = "Help", menu = helpmenu)
    set_page.config(menu=menubar)
    Buttont1 = Button(text ="Next", command = chapter2page2 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter2page2():
    """once of chapter2 page"""
    photo = PhotoImage(file="logic2.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter2page3 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter2page3():
    """once of chapter2 page"""
    photo = PhotoImage(file="logic3.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter2page4 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter2page4():
    """once of chapter2 page"""
    photo = PhotoImage(file="logic4.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter2page5 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter2page5():
    """once of chapter2 page"""
    photo = PhotoImage(file="logic5.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter2page6 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter2page6():
    """once of chapter2 page"""
    photo = PhotoImage(file="logic6.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter2page7 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter2page7():
    """once of chapter2 page"""
    photo = PhotoImage(file="logic7.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter2page8 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter2page8():
    """once of chapter2 page"""
    photo = PhotoImage(file="logic8.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter2page9 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter2page9():
    """once of chapter2 page"""
    photo = PhotoImage(file="logic9.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter2page10 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter2page10():
    """once of chapter2 page"""
    photo = PhotoImage(file="logic10.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter2page11 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter2page11():
    """once of chapter2 page"""
    photo = PhotoImage(file="logic11.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter2page12 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter2page12():
    """once of chapter2 page"""
    photo = PhotoImage(file="logic12.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter2page13 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter2page13():
    """once of chapter2 page"""
    photo = PhotoImage(file="logic13.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter2page14 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter2page14():
    """once of chapter2 page"""
    photo = PhotoImage(file="logic14.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter2page15 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter2page15():
    """once of chapter2 page"""
    photo = PhotoImage(file="logic15.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter2page16 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter2page16():
    """once of chapter2 page"""
    photo = PhotoImage(file="logic16.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter2page17 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter2page17():
    """once of chapter2 page"""
    photo = PhotoImage(file="logic17.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter2page18 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter2page18():
    """once of chapter2 page"""
    photo = PhotoImage(file="logic18.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter2page19 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter2page19():
    """once of chapter2 page"""
    photo = PhotoImage(file="logic19.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter2page20 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter2page20():
    """once of chapter2 page"""
    photo = PhotoImage(file="logic20.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = test2page1 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def test2page1():
    """test chap2 page1"""
    photo = PhotoImage(file="logic_quiz1.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Yes", command = correct3 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 110, y = 60)
    Buttont2 = Button(text ="No", command = wrong , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 180, y = 60)
    Buttont3 = Button(text ="Yes", command = correct3 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 110, y = 155)
    Buttont4 = Button(text ="No", command = wrong , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 180, y = 155)
    Buttont5 = Button(text ="Yes", command = correct3 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 110, y = 253)
    Buttont6 = Button(text ="No", command = wrong , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 180, y = 253)
    Buttont7 = Button(text ="Yes", command = wrong , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 110, y = 348)
    Buttont8 = Button(text ="No", command = correct3 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 180, y = 348)
    Buttont9 = Button(text ="Yes", command = wrong , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 110, y = 440)
    Buttont10 = Button(text ="No", command = correct3 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 180, y = 440)
    Buttont11 = Button(text ="Yes", command = correct3 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 110, y = 535)
    Buttont12 = Button(text ="No", command = wrong , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 180, y = 535)
    Buttont13 = Button(text ="Next", command = ans_page3 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 775, y = 550)

def ans_page3():
    """solver for test chapter2"""
    photo = PhotoImage(file="logic_quiz1ans.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = back , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 750, y = 498)

def correct3():
    """only reply correct"""
    tkMessageBox.showinfo("Answer", "Correct!!")

def chapter3():
    """Chapter3"""
    homepage.destroy()
    global set_page
    set_page = Tk()
    set_page.geometry('875x600')
    photo = PhotoImage(file="reasoning.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    menubar = Menu(set_page)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command = close_set)
    menubar.add_cascade(label = "File", menu = filemenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Instuction")
    helpmenu.add_separator()
    helpmenu.add_command(label="Credits", command = credit)
    menubar.add_cascade(label = "Help", menu = helpmenu)
    set_page.config(menu=menubar)
    Buttont1 = Button(text ="Next", command = chapter3page2 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter3page2():
    """once of chapter3 page"""
    photo = PhotoImage(file="reasoning2.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter3page3 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter3page3():
    """once of chapter3 page"""
    photo = PhotoImage(file="reasoning3.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter3page4 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter3page4():
    """once of chapter3 page"""
    photo = PhotoImage(file="reasoning4.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter3page5 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter3page5():
    """once of chapter3 page"""
    photo = PhotoImage(file="reasoning5.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter3page6 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def chapter3page6():
    """once of chapter3 page"""
    photo = PhotoImage(file="reasoning6.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = test_chap3 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def test_chap3():
    """test by using typing for answer"""
    photo = PhotoImage(file="reason_quiz1.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    global dummy
    dummy = StringVar()
    global dummy2
    dummy2 = StringVar()
    dummy.set('answer here')
    dummy2.set('answer here')
    mntry = Entry(set_page, textvariable = dummy, fg = 'black', bg = 'yellow').place(x = 115, y = 330)
    mntry2 = Entry(set_page, textvariable = dummy2, fg = 'black', bg = 'yellow').place(x = 115, y = 430)
    Buttontx1 = Button(text ="commit", command = commit_ans , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)

def commit_ans():
    dummyxx = dummy.get()
    dummyxx2 = dummy2.get()
    count = 0
    if dummyxx == '21':
        texti = Label(set_page, text = 'Correct', fg = 'black', bg = 'yellow').place(x = 285, y = 330)
        count += 1
    else:
        texti = Label(set_page, text = 'Wrong!', fg = 'black', bg = 'yellow').place(x = 285, y = 330)
    if dummyxx2 == 'No':
        texti = Label(set_page, text = 'Correct', fg = 'black', bg = 'yellow').place(x = 285, y = 430)
        count += 1
    else:
        texti = Label(set_page, text = 'Wrong!', fg = 'black', bg = 'yellow').place(x = 285, y = 430)
    if count == 2:
        Buttont2 = Button(text ="Next", command = back , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 450)

homepagedef()
##import sys
##from Tkinter import *
##import tkMessageBox ##Reply massage box
##
##mGui = Tk()
##dummy = StringVar()
##
##mGui.geometry('600x400')
##mGui.title("Test Tkinter")
##def helloCallBack(): ##Reply massage box
##    tkMessageBox.showinfo( "HEAD LINE", "my first testing TKinter") ##Reply massage box
##    texti2 = Label(mGui, text = 'For testing place', fg = 'white', bg = 'black').place(x = 100, y = 100)
##    texti3 = Label(mGui, text = 'For testing place', fg = 'white', bg = 'blue').place(x = 100, y = 200)
##    texti4 = Label(mGui, text = 'For testing place', fg = 'black', bg = 'red').place(x = 200, y = 100)
##texti = Label(text = 'For testing', fg = 'white', bg = 'black').pack() ##for text
###texti5 = Label(text = 'For testing grid', fg = 'white', bg = 'black').grid(row =0, column =0, sticky =w)
###texti6 = Label(text = 'For testing grid', fg = 'white', bg = 'blue').grid(row =1, column =0)
###texti7 = Label(text = 'For testing grid', fg = 'black', bg = 'red').grid(row =0, column =1)
##B = Button(text ="Button", command = helloCallBack, fg = 'white', bg = 'red') ##button Reply massage box
##B.pack() ##For Showing the Button or another
##
##texti = Label(text = 'For testing button and entry', fg = 'white', bg = 'black').pack()
####dummy = StringVar()
##def test_entry():
##    mntry = Entry(mGui, textvariable = dummy).pack()
##    mbutton = Button(mGui, text = 'ok', command = showdummy).pack()
##
##def showdummy():
##    mtext = dummy.get()
##    texti2 = Label(text = mtext, fg = 'white', bg = 'black').pack()
##    
##mbutton = Button(mGui, text = 'text', command = test_entry).pack()
##
##menubar = Menu(mGui)
##
##filemenu = Menu(menubar)
##filemenu.add_command(label="New")
##filemenu.add_command(label="Open")
##filemenu.add_command(label="Save As...")
##filemenu.add_command(label="Close")
##
##menubar.add_cascade(label = "file", menu = filemenu)
##
##mGui.config(menu=menubar)
##
##mGui.mainloop()       
