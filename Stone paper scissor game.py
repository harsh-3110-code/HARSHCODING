from datetime import datetime
print("STONE PAPER SCISSOR GAME")
print("enter s for stone \nenter p for paper \nenter sc for scissor")
i=10
x=0
y=0
def record(msg):
    with open("sps_record.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

while(1):
    a=input("enter your choice ")
    import random
    list=["s","p","sc"]
    choice = random.choice(list)
    print("computer select", choice)
    if a=="s" and choice=="p":
        print("computer wins")
        x=x+1
        print("computer have ",x," points and you have ",y," points")
        if i>0:
            i=i-1
            print(i," game is left")
        else:
            break
        continue
    elif a=="s" and choice=="sc":
        print("you win")
        y = y + 1
        print("computer have ", x, " points and you have ", y, " points")
        if i>0:
            i=i-1
            print(i, " game is left")
        else:
            break
        continue
    elif a=="s" and choice=="s":
        print("draw")
        print("computer have ", x, " points and you have ", y, " points")
        if i>0:
            i=i-1
            print(i," game is left")
        else:
            break
        continue
    elif a=="p" and choice=="sc":
        print("computer wins")
        x = x + 1
        print("computer have ", x, " points and you have ", y, " points")
        if i>0:
            i=i-1
            print(i, " game is left")
        else:
            break
        continue
    elif a=="p" and choice=="s":
        print("you win")
        y = y + 1
        print("computer have ", x, " points and you have ", y, " points")
        if i>0:
            i=i-1
            print(i, " game is left")
        else:
            break
        continue
    elif a=="p" and choice=="p":
        print("draw")
        print("computer have ", x, " points and you have ", y, " points")
        if i>0:
            i=i-1
            print(i," game is left")
        else:
            break
        continue
    elif a=="sc" and choice=="sc":
        print("draw")
        print("computer have ", x, " points and you have ", y, " points")
        if i>0:
            i=i-1
            print(i," game is left")
        else:
            break
        continue
    elif a=="sc" and choice=="p":
        print("you win")
        y = y + 1
        print("computer have ", x, " points and you have ", y, " points")
        if i>0:
            i=i-1
            print(i, " game is left")
        else:
            break
        continue
    elif a=="sc" and choice=="s":
        print("computer wins")
        x = x + 1
        print("computer have ", x, " points and you have ", y, " points")
        if i>0:
            i=i-1
            print(i, " game is left")
        else:
            break
        continue
    else:
        print("invalid choice")
    continue
if x>y:
    print("computer win the series")
    print(record("100 points to COMPUTER"))
elif y>x:
    print("you won the series")
    print(record("100 points to YOU"))
else:
    print("draw")
    print(record("no points recorded since the game is DRAW"))