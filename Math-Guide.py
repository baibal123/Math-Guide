"""Math-Guide the project 3/12/2557 AM2.11"""
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

##def pow_set(setnumber):
##    """Make power set from set"""
##    setnumber = same_member(setnumber)
##    for i in setnumber: ##waiting for solving if 4+ member
##        box.append(i)
##        for j in setnumber:
##            if i != j:
##                box.append(i, j)

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
