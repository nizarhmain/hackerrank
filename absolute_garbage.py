def converto(boi):
    if "PM" in boi:
        if int(boi[0:2]) == 12:
            print(boi[:-2])
        else:
            x = int(boi[0:2]) + 12
            if x >= 24:
                y = (boi.replace(boi[0:2],"00"))
                print(y[:-2])
            else:
                y = (boi.replace(boi[0:2],str(x)))
                print(y[:-2])
    else:
        if boi[0:2] == "12":
            y = (boi.replace(boi[0:2],"00"))
            print(y[:-2])
        else:
            print(boi[:-2])
       
converto("12:13:05PM")


