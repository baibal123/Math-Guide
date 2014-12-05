"""Math-Guide the project 6/12/2557 AM0.50+"""
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
