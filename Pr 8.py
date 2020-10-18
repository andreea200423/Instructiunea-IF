a=int(input("Primul nr este"))
b=int(input("Al doilea nr este"))
if (a%2==0) and (b%2==0):
    if a>=b:
        print(a)
    else:
        print(b)
else:
    print("Nr nu sunt")