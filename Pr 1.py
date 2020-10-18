a=(input("Nr curent pu primul elev: "))
x=(input("Punctajul pu primul elev: "))
b=(input("Nr curent pu al doilea elev: "))
y=(input("Punctajul pu al doilea elev: "))
c=(input("Nr curent al treilea elev: "))
z=(input("Punctajul al treilea elev: "))
if(y>x) and (y>z):
    print("Punctajul max il are elevul cu nr curent ", b)
if(z>y) and (z>x):
    print("Punctajul max il are elevul cu nr curent ", c)
if(x>y) and (x==z):
    print("Punctajul max il are elevul cu nr curent ", a)
if(x==y) and (x>z):
    print("Punctajul max il are elevul cu nr curent ", a)
if(x==y) and (x==z):
    print("Punctajul max il are elevul cu nr curent ", a)