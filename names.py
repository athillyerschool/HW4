def generateName(first, last):
    if(type(first) != str or type(last) != str):
        return str("Not a valid type.")
    if(any(char.isdigit() for char in first) or any(char.isdigit() for char in last)):
        return str("Name can't contain numbers.")
    return str(first + " " + last)