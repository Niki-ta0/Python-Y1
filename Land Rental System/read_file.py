def opening():
    f = open("Coursework.txt", "r")
    temp = []
    for each in f:
        ff = each.replace("\n", "")
        temp.append(ff.split(","))
    return temp
