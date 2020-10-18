a=int(input("Primul nr e"))
b=int(input("Al doilea nr e"))
c=int(input("Al treilea nr e"))
if (a>0) and (b>0) and (c>0):
    if b>=c:
        print(b)
    else:
        print(c)
else :
    print(a+b)