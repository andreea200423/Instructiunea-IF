A=int(input("Nr de bilete albe mari"))
a=int(input("Nr de bilete albe mici"))
R=int(input("Nr de bilete rosii mari"))
r=int(input("Nr de bilete rosii mici"))
V=int(input("Nr de bilete verzi mari"))
v=int(input("Nr de bilete verzi mici"))
print("In total sunt", A+a+R+r+V+v, "bile")
if(A+R+V)>(a+r+v):
    print("Sunt mai multe bile mari fiind", A+R+V)
elif(A+R+V)<(a+r+v):
    print("Sunt mai multe bile mici fiind", a+rv)
else:
    print("Numarul de bile mari e egal cu numarul de bile mici, fiind", A+R+V)
if(A>a>=R>r) and (A>a>=V+v):
    print("Bilele cele mai numeroase sunt de culoare alba, fiind", A+a)
elif(R+r>=A+a) and (R+r>+V+v):
    print("Bilele cele mai numeroase sunt de culoare rosie, fiind", R+r)
else:
    print("Bilele cele mai numeroase sunt de culoare verde, fiind", V+v)
