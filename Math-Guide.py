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
    Button4 = Button(text ="Chapter 4 - Real Number", command = chapter4 , fg = 'black', bg = 'yellow', height = 2, width = 63).grid(row =4, column =0, sticky = W)
    Button5 = Button(text ="Chapter 5 - Number Theory", command = chapter5 , fg = 'black', bg = 'yellow', height = 2, width = 63).grid(row =5, column =0, sticky = W)
    texti = Label(text = 'test-->Chapter', fg = 'yellow', bg = 'black', height = 3, width = 20).grid(row =6, column =0, sticky = W)
    Buttont1 = Button(text ="1", command = test1page1gui , fg = 'yellow', bg = 'black', height = 3, width = 5).place(x = 146, y = 298)
    Buttont2 = Button(text ="2", command = test2page1gui , fg = 'yellow', bg = 'black', height = 3, width = 5).place(x = 191, y = 298)
    Buttont3 = Button(text ="3", command = test3page1gui , fg = 'yellow', bg = 'black', height = 3, width = 5).place(x = 236, y = 298)
<<<<<<< HEAD
    Buttont4 = Button(text ="4", command = donothing , fg = 'yellow', bg = 'black', height = 3, width = 5).place(x = 281, y = 298)
    Buttont5 = Button(text ="5", command = test5page1gui , fg = 'yellow', bg = 'black', height = 3, width = 5).place(x = 326, y = 298)
=======
    Buttont4 = Button(text ="4", command = test4page1 , fg = 'yellow', bg = 'black', height = 3, width = 5).place(x = 281, y = 298)
    Buttont5 = Button(text ="5", command = test5page1 , fg = 'yellow', bg = 'black', height = 3, width = 5).place(x = 326, y = 298)
    Buttont6 = Button(text ="Final", command = donothing , fg = 'yellow', bg = 'black', height = 3, width = 10).place(x = 371, y = 298)
>>>>>>> 7ab7a69f44a1733bdfa4eb4b5b07ede9a8ed5605

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
    tkMessageBox.showinfo("Credits", "Math-Guide V.1.0 create by baibal123(57070040), Rycan(57070120)")

def closehomepage():
    """Menu-->Exit the program"""
    exits = tkMessageBox.askyesno('Exit', 'Are you sure?')
    if exits > 0:
        homepage.destroy()

def chapter1():
    """Chapter one recreate new window"""
    homepage.destroy()
    global set_page, page, chap1
    chap1 = ["Set_page1.gif", "Set_page2.gif", "Set_page3.gif", "Set_page4.gif", "Set_page5.gif", "Set_page6.gif", "Set_page7.gif"]
    page = 0
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
    Buttont1 = Button(text ="Next", command = nextpage1 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)
    Backhome = Button(text ="HOME", command = back, fg = 'black', bg = 'lightblue', height = 2, width = 10).place(x = 775, y = 15)
    Backpage = Button(text ="Back", command = back, fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 15, y = 550)

def nextpage1():
    """control page to show"""
    global page, chap1
    page += 1
    if page >= len(chap1):
        test1page1()
    else:
        chapter1page(page)

def backpage1():
    """control back page to show"""
    global page, chap1
    page -= 1
    if page < 0:
        back()
    else:
        chapter1page(page)

def chapter1page(page):
    """once of page"""
    global chap1
    photo = PhotoImage(file=chap1[page])
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = nextpage1 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)
    Backhome = Button(text ="HOME", command = back, fg = 'black', bg = 'lightblue', height = 2, width = 10).place(x = 775, y = 15)
    Backpage = Button(text ="Back", command = backpage1, fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 15, y = 550)
    
def close_set():
    """Exit the program while in chapter"""
    exits = tkMessageBox.askyesno('Exit', 'Are you sure?')
    if exits > 0:
        set_page.destroy()

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

def test5page1gui():
    """test page but run from interface"""
    homepage.destroy()
    global set_page
    set_page = Tk()
    set_page.geometry('875x600')
    photo = PhotoImage(file="theoryquiz.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Answer", command = answer5 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)
    Backhome = Button(text ="HOME", command = back, fg = 'black', bg = 'lightblue', height = 2, width = 10).place(x = 15, y = 550)
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
    """Chapter one recreate new window"""
    homepage.destroy()
    global set_page, page, chap2
    chap2 = ["logic1.gif", "logic2.gif", "logic3.gif", "logic4.gif", "logic5.gif", "logic6.gif", "logic7.gif",\
             "logic8.gif", "logic9.gif", "logic10.gif", "logic11.gif", "logic12.gif", "logic13.gif", "logic14.gif",\
             "logic15.gif", "logic16.gif", "logic17.gif", "logic18.gif", "logic19.gif", "logic20.gif"]
    page = 0
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
    Buttont1 = Button(text ="Next", command = nextpage2 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)
    Backhome = Button(text ="HOME", command = back, fg = 'black', bg = 'lightblue', height = 2, width = 10).place(x = 775, y = 15)
    Backpage = Button(text ="Back", command = back, fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 15, y = 550)

def nextpage2():
    """control page to show"""
    global page, chap2
    page += 1
    if page >= len(chap2):
        test2page1()
    else:
        chapter2page(page)

def backpage2():
    """control back page to show"""
    global page, chap2
    page -= 1
    if page < 0:
        back()
    else:
        chapter2page(page)

def chapter2page(page):
    """once of page"""
    global chap2
    photo = PhotoImage(file=chap2[page])
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = nextpage2 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)
    Backhome = Button(text ="HOME", command = back, fg = 'black', bg = 'lightblue', height = 2, width = 10).place(x = 775, y = 15)
    Backpage = Button(text ="Back", command = backpage2, fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 15, y = 550)
  
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
    """Chapter one recreate new window"""
    homepage.destroy()
    global set_page, page, chap3
    chap3 = ["reasoning.gif", "reasoning2.gif", "reasoning3.gif", "reasoning4.gif", "reasoning5.gif", "reasoning6.gif"]
    page = 0
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
    Buttont1 = Button(text ="Next", command = nextpage3 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)
    Backhome = Button(text ="HOME", command = back, fg = 'black', bg = 'lightblue', height = 2, width = 10).place(x = 775, y = 15)
    Backpage = Button(text ="Back", command = back, fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 15, y = 550)
  
def nextpage3():
    """control page to show"""
    global page, chap3
    page += 1
    if page >= len(chap3):
        test_chap3()
    else:
        chapter3page(page)

def backpage3():
    """control back page to show"""
    global page, chap3
    page -= 1
    if page < 0:
        back()
    else:
        chapter3page(page)


def chapter3page(page):
    """once of page"""
    global chap3
    photo = PhotoImage(file=chap3[page])
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = nextpage3 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)
    Backhome = Button(text ="HOME", command = back, fg = 'black', bg = 'lightblue', height = 2, width = 10).place(x = 775, y = 15)    
    Backpage = Button(text ="Back", command = backpage3, fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 15, y = 550)

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

def chapter4():
    """Chapter one recreate new window"""
    homepage.destroy()
    global set_page, page, chap4
    chap4 = ["real1.gif", "real2.gif", "real3.gif", "real4.gif", "real5.gif", "real6.gif", "real7.gif",\
             "real8.gif", "real9.gif", "real10.gif", "real11.gif", "real12.gif", "real13.gif", "real14.gif",\
             "real15.gif", "real16.gif", "real17.gif", "real18.gif", "real19.gif", "real20.gif", ]
    page = 0
    set_page = Tk()
    set_page.geometry('875x600')
    photo = PhotoImage(file="real1.gif")
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
    Buttont1 = Button(text ="Next", command = nextpage4 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)
    Backhome = Button(text ="HOME", command = back, fg = 'black', bg = 'lightblue', height = 2, width = 10).place(x = 775, y = 15)
    Backpage = Button(text ="Back", command = back, fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 15, y = 550)


def nextpage4():
    """control page to show"""
    global page, chap4
    page += 1
    if page >= len(chap4):
        back()
    else:
        chapter4page(page)

def backpage4():
    """control back page to show"""
    global page, chap4
    page -= 1
    if page < 0:
        test4page1()
    else:
        chapter4page(page)


def chapter4page(page):
    """once of page"""
    global chap4
    photo = PhotoImage(file=chap4[page])
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = nextpage4 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)
    Backhome = Button(text ="HOME", command = back, fg = 'black', bg = 'lightblue', height = 2, width = 10).place(x = 775, y = 15)    
    Backpage = Button(text ="Back", command = backpage4, fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 15, y = 550)

def test4page1():
    """quiz for number theory substance"""
    photo = PhotoImage(file="realquiz.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Answer", command = answer5 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)
    Backhome = Button(text ="HOME", command = back, fg = 'black', bg = 'lightblue', height = 2, width = 10).place(x = 15, y = 550)

def answer5():
    photo = PhotoImage(file="ansreal.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Backhome = Button(text ="HOME", command = back, fg = 'black', bg = 'lightblue', height = 2, width = 10).place(x = 775, y = 15)    
    Backpage = Button(text ="Back", command = test5quiz, fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 15, y = 550)

def chapter5():
    """Chapter one recreate new window"""
    homepage.destroy()
    global set_page, page, chap5
    chap5 = ["numbertheory1.gif", "numbertheory2.gif", "numbertheory3.gif", "numbertheory4.gif", "numbertheory5.gif",\
             "numbertheory6.gif", "numbertheory7.gif", "numbertheory8.gif", "numbertheory9.gif", "numbertheory10.gif",\
             "numbertheory11.gif", "numbertheory12.gif", "numbertheory13.gif", "numbertheory14.gif", "numbertheory15.gif",\
             "numbertheory16.gif", ]
    page = 0
    set_page = Tk()
    set_page.geometry('875x600')
    photo = PhotoImage(file="numbertheory1.gif")
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
    Buttont1 = Button(text ="Next", command = nextpage5 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)
    Backhome = Button(text ="HOME", command = back, fg = 'black', bg = 'lightblue', height = 2, width = 10).place(x = 775, y = 15)
    Backpage = Button(text ="Back", command = back, fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 15, y = 550)


def nextpage5():
    """control page to show"""
    global page, chap5
    page += 1
    if page >= len(chap5):
        back()
    else:
        chapter5page(page)

def backpage5():
    """control back page to show"""
    global page, chap5
    page -= 1
    if page < 0:
        test5page1()
    else:
        chapter5page(page)


def chapter5page(page):
    """once of page"""
    global chap5
    photo = PhotoImage(file=chap5[page])
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = nextpage5 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)
    Backhome = Button(text ="HOME", command = back, fg = 'black', bg = 'lightblue', height = 2, width = 10).place(x = 775, y = 15)    
    Backpage = Button(text ="Back", command = backpage5, fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 15, y = 550)

def test5page1():
    """quiz for number theory substance"""
    photo = PhotoImage(file="theoryquiz.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Answer", command = answer5 , fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 775, y = 550)
    Backhome = Button(text ="HOME", command = back, fg = 'black', bg = 'lightblue', height = 2, width = 10).place(x = 15, y = 550)

def answer5():
    photo = PhotoImage(file="anstheory.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Backhome = Button(text ="HOME", command = back, fg = 'black', bg = 'lightblue', height = 2, width = 10).place(x = 775, y = 15)    
    Backpage = Button(text ="Back", command = test5quiz, fg = 'black', bg = 'yellow', height = 2, width = 10).place(x = 15, y = 550)

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
