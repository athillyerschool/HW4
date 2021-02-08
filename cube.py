
def volumeCube(length, width, height):
    try:
        return float(float(length)*float(width)*float(height))
    except ValueError:
        return None
