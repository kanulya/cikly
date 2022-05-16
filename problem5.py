i = 1
a = True
while True:
    if a == True:
        if i == 10:
            a = False
        else:
            print(i, end=" ")
            i += 1
    else:
        if i == 0:
            break
        print(i, end=" ")
        i -= 1
