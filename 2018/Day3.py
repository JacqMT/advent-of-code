f = open(r"2018/assets/fabricClaims.txt")

claimRectangles = []

for claim_entry in f.readlines():
    claim = claim_entry.replace(' ', '')
    claimId, rectangle_info = claim.split('@')
    placement, measurement = rectangle_info.split(':')

    leftMargin = int(placement.split(',')[0])
    topMargin = int(placement.split(',')[1])

    # Account for starting square by - 1
    width = int(measurement.split('x')[0])-1
    height = int(measurement.split('x')[1])-1

    claimRectangles.append({
        'topLeft': [leftMargin, topMargin],
        'topRight': [leftMargin+width, topMargin],
        'bottomLeft': [leftMargin,topMargin+height],
        'bottomRight': [leftMargin+width, topMargin+height]
    })

# Checks if any corner of rect_two is contained within the bounds of rect_one and if so returns square measurement of overlap
def overlaps(rect_one, rect_two):
    if rect_two['topLeft'][0] < rect_one['topRight'][0] and rect_two['topLeft'][0] > rect_one['topLeft'][0] and rect_two['topLeft'][1] < rect_one['topRight'][1] and rect_two['topLeft'][1] > rect_one['bottomRight'][1]:
        return (rect_two['topLeft'][0] - rect_one['topLeft'][0]) * (rect_two['topLeft'][1] - rect_one['bottomRight'][1])

    if rect_two['topRight'][0] < rect_one['topRight'][0] and rect_two['topRight'][1] > rect_one['bottomLeft'][0] and rect_two['topRight'][1] < rect_one['topLeft'][1] and rect_two['topRight'][1] > rect_one['bottomLeft'][1]:
        return (rect_two['topRight'][0] - rect_one['bottomLeft'][0]) * (rect_two['topRight'][1] - rect_one['bottomLeft'][1])

    if rect_two['bottomRight'][0] < rect_one['topRight'][0] and rect_two['bottomRight'][0] > rect_one['topLeft'][0] and rect_two['bottomRight'][1] < rect_one['bottomLeft'][1] and rect_two['bottomRight'][1] < rect_one['topLeft'][1]:
        return (rect_two['bottomRight'][0] - rect_one['topRight'][0]) * (rect_two['bottomRight'][1] - rect_one['topLeft'][1])
    
    if rect_two['bottomLeft'][0] < rect_one['topRight'][0] and rect_two['bottomLeft'][0] > rect_one['topLeft'][0] and rect_two['bottomLeft'][1] < rect_one['bottomRight'][1] and rect_two['bottomLeft'] > rect_one['topRight'][1]:
        return (rect_two['bottomLeft'][0] - rect_one['topLeft'][0]) * (rect_two['bottomLeft'][1] - rect_one['topRight'][1])

    return 0

overlap = 0
for i in range(len(claimRectangles)-1):
    for j in range(i+1,len(claimRectangles)):
        rect_one = claimRectangles[i]
        rect_two = claimRectangles[j]
        overlap += overlaps(rect_one, rect_two)
        if overlap:
            print(rect_one)
            print(rect_two)
            print(overlap)
            exit()

print(overlap)
