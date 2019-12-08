f = open(r"2018/assets/boxIds.txt")

one = ""
two = ""
ids = []
for boxId in f.readlines():
    ids.append(boxId)

foundMatch = False
for first_id in ids:
    if foundMatch: break
    for second_id in ids:
        if foundMatch: break
        if first_id == second_id: continue
        diffs = 0
        letters = []
        for i in range(len(first_id)-1):
            if not first_id[i] == second_id[i]: diffs +=1
            else: letters.append(first_id[i])
        if diffs == 1:
            foundMatch = True
            print("".join(letters))
            break