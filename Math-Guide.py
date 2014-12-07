"""Math-Guide the project 7/12/2557 PM10.06+"""
##______________Tkinter zone_____________________________

import sys
from Tkinter import *
import tkMessageBox ##Reply massage box

mGui = Tk()
mGui.geometry('600x400')
mGui.title("Test Tkinter")
def helloCallBack(): ##Reply massage box
    tkMessageBox.showinfo( "Hello Python", "Hello World") ##Reply massage box
B = Button(text ="Button", command = helloCallBack) ##button Reply massage box
B.pack()
mGui.mainloop()
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
