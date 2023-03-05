namai_wa = ["Dice", "L", "Lelouch", "Zoro", "Kenpachi", "Orochimaru", "Nagato", "Neferpitou"]

def reverse1(namai_wa):
    for each in range(len(namai_wa)):
        swap = namai_wa.pop(-1)
        print(namai_wa)
        namai_wa.insert(0,swap)
    print(namai_wa)

def move_it2(namai_wa):

    for each in range(0, len(namai_wa)):
        if each ==1: 
            hold = namai_wa[-each]
            namai_wa[-each] = namai_wa[each]
            namai_wa[each] = hold

def reverse(namai_wa):
    #just swap the first element at the end 
    #what if its an even number of elements. just check?
    print(namai_wa)
    n = len(namai_wa)
    for x in range(0, n//2):
        box = namai_wa[x]
        namai_wa[x] = namai_wa[n-1-x]
        namai_wa[n-1-x] = box
        print(namai_wa)
    print(namai_wa)

reverse(namai_wa)
"""
what if we had a start posi that differs depending on the nature of the list (even or positive intgers)
bun the negatibe indices, ust do posi - length
"""



"""
take nth posi
sub from (length of list -1)
insert it as so 
then smn from there on
"""

"""might be  container type beat"""