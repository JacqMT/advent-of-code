
f = open(r"2018/assets/shifts.txt")
changes = []
for line in f.readlines():
    changes.append(int(line))

freq = 0
freqs = [freq]
index = 0
while index <= len(changes):
    if index == len(changes):
        index = 0
    freq += changes[index]
    if freq in freqs:
        print("Duplicate frequency found: " + str(freq))
        break
        
    freqs.append(freq)
    index+=1