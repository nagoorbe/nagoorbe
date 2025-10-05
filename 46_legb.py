x = "global"

def outer():
    x = "enclosed"
    def inner():
        x = "local"
        print("inside  Inner:", x) 
    inner()
    print("inside Outer :", x)      

outer()
print("At Global :", x)        
