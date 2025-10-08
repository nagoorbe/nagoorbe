numbers=[10,20,30,40]
with open("num.txt","w") as f:
    for n in numbers:
        f.write(str(n) + "\n")