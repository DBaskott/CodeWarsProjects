def opposite(number):
    if number < 0: 
        number = abs(number)
    else:
        number = -abs(number)
    return number
