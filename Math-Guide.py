"""Math-Guide the project 8/12/2557 PM6.26+"""
##______________Tkinter zone_____________________________
import sys
from Tkinter import *
import tkMessageBox
def homepagedef():
    global homepage
    homepage = Tk()
    homepage.geometry('450x350')
    photo = PhotoImage(file="Teammy.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Button1 = Button(text ="Chapter 1 - Set", command = chapter1 , fg = 'black', bg = 'yellow', height = 2, width = 63).grid(row =1, column =0, sticky = W)
    Button2 = Button(text ="Chapter 2 - propositional logic", command = donothing , fg = 'black', bg = 'yellow', height = 2, width = 63).grid(row =2, column =0, sticky = W)
    Button3 = Button(text ="Chapter 3 - propositional logic", command = donothing , fg = 'black', bg = 'yellow', height = 2, width = 63).grid(row =3, column =0, sticky = W)
    Button4 = Button(text ="Chapter 4 - propositional logic", command = donothing , fg = 'black', bg = 'yellow', height = 2, width = 63).grid(row =4, column =0, sticky = W)
    Button5 = Button(text ="Chapter 5 - propositional logic", command = donothing , fg = 'black', bg = 'yellow', height = 2, width = 63).grid(row =5, column =0, sticky = W)
    texti = Label(text = 'test-->Chapter', fg = 'yellow', bg = 'black', height = 3, width = 20).grid(row =6, column =0, sticky = W)
    Buttont1 = Button(text ="1", command = donothing , fg = 'yellow', bg = 'black', height = 3, width = 5).place(x = 146, y = 298)
    Buttont2 = Button(text ="2", command = donothing , fg = 'yellow', bg = 'black', height = 3, width = 5).place(x = 191, y = 298)
    Buttont3 = Button(text ="3", command = donothing , fg = 'yellow', bg = 'black', height = 3, width = 5).place(x = 236, y = 298)
    Buttont4 = Button(text ="4", command = donothing , fg = 'yellow', bg = 'black', height = 3, width = 5).place(x = 281, y = 298)
    Buttont5 = Button(text ="5", command = donothing , fg = 'yellow', bg = 'black', height = 3, width = 5).place(x = 326, y = 298)
    Buttont6 = Button(text ="Final", command = donothing , fg = 'yellow', bg = 'black', height = 3, width = 10).place(x = 371, y = 298)

    menubar = Menu(homepage)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Score")
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command = closehomepage)
    menubar.add_cascade(label = "File", menu = filemenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Instuction")
    helpmenu.add_separator()
    helpmenu.add_command(label="Credits", command = credit)
    menubar.add_cascade(label = "Help", menu = helpmenu)

    homepage.config(menu=menubar)
    homepage.mainloop()
    
def donothing():
    pass

def credit():
    tkMessageBox.showinfo("Credits", "Math-Guide V.1.0 create by baibal123(57070040)")

def closehomepage():
    exits = tkMessageBox.askyesno('Exit', 'Are you sure?')
    if exits > 0:
        homepage.destroy()

def chapter1():
    homepage.destroy()
    set_page = Tk()
    global set_page
    set_page.geometry('875x600')
    photo = PhotoImage(file="Set_page1.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = chapter1page2 , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 750, y = 498)

def chapter1page2():
    photo = PhotoImage(file="Set_page2.gif")
    label = Label(image=photo)
    label.image = photo
    label.grid(row =0, column =0)
    Buttont1 = Button(text ="Next", command = donothing , fg = 'black', bg = 'yellow', height = 2, width = 5).place(x = 750, y = 498)

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
##
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
##________________SET____________________________________

def npowset_set(setnumber):
    """Find how many member in power set v.set"""
    return len(setnumber)**2

def npowset_n(number):
    """Find how many member in power set v.number"""
    return number**2

def same_member(setnumber):
    """Cutout the same member because set not count"""
    box = []
    for i in setnumber:
        if i not in box:
            box.append(i)
    return box

def list_powerset(box):
    """Find powerset"""
    result = [[]]
    for i in same_member(box):
        result.extend([subset + [i] for subset in result])
    return result

def is_subset():
    """check subset list to list"""
    main = input()
    checkset = input()
    if main == list and checkset != list:
        return False
    for i in checkset:
        if i not in main:
            return False
    return True

def is_member():
    """
    this function use for check member
    input = 1.list of set
            2.only 1 number for check
    """
    main = input()
    checknumber = input()
    if main == list and checkset == list:
        return False
    if checknumber not in main:
        return False
    return True

def union(box, box2):
    """union set fuction"""
    for i in box2:
        box.append(i)
    return same_member(box)

def inter_and_com(box, box2):
    """
    this function can use for intersect and Compliment in one
    if you want to use for Compliment you replace 'box' with universe
    and 'box2' is what ever set that you want to compliment
    but normaly i made this function for intersection so box is mainset
    and box2 is set that use for remove from set one
    """
    for i in box2:
        if i in box:
            box.remove(i)
    return box

##______________Prapod___propositional logic_______________

def not_pl(word):
    """logic function for change into opposite"""
    if word == True:
        return False
    else:
        return True

def and_pl(word, word2):
    """logic function for check if word one and two are True"""
    if word == True and word2 == True:
        return True
    else:
        return False

def or_pl(word, word2):
    """
    logic function for check word one and two are False and return themself
    """
    if word == False and word2 == False:
        return False
    else:
        return True

def if_so_pl(word, word2):
    """
    logic function for check if word(True) so word2(False)
    it will return False
    """
    if word == True and word2 == False:
        return False
    else:
        return True

def when_pl(word, word2):
    """logic function for check if word one and two are the same"""
    if word == word2:
        return True
    else:
        return False

##def in_one_line: waiting for solving....            
