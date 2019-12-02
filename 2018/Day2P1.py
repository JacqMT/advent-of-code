f = open(r"2018/assets/boxIds.txt")

twiceLetter = 0
thriceLetter = 0
for boxId in f.readlines():
    chars = set(boxId)
    hasCheckedForTwo = False
    hasCheckedForThree = False
    for letter in chars:
        occ = boxId.count(letter)
        if occ == 2 and not hasCheckedForTwo:
            twiceLetter+=1
            hasCheckedForTwo = True
        if occ == 3 and not hasCheckedForThree:
            thriceLetter+=1
            hasCheckedForThree = True

print(twiceLetter*thriceLetter)