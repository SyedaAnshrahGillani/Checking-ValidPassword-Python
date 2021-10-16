c1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
c2=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
c3=["0","1","2","3","4","5","6","7","8","9"]
c4=["$","#","@"]

minimum=6
maximum=12

while True:
    p=input("Enter password: ")
    for i in p:
        if i in c1 :
            b=True
        if i in c2:
            b1=True
        if i in c3:
            b2=True
        if i in c4:
            b3=True
    if len(p)>6 and len(p)<12:
        b4=True
    if b and b1 and b2 and b3 and b4: #ANY ERROR AFTER RUNNING THE CODE
        print("Valid password!")       #INDICATES INVALID PASSWORD
        break
    else:
        print("Invalid password!")
