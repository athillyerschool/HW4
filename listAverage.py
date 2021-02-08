def average(thisList):
    length = len(thisList)
    total = 0
    if(length == 0):
        return None
    for position in range(len(thisList)):
        total = total + thisList[position]
    
    average = float(total)/float(length)

    return average